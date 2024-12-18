# backend/battery_simulation.py
import pybamm

def run_simulation(battery_model: str, params: dict):
    model = getattr(pybamm, battery_model, None)()
    if not model:
        raise ValueError(f"Battery model {battery_model} not found")
    parameter_values = pybamm.ParameterValues("Marquis2019")
    parameter_values.update(params)
    sim = pybamm.Simulation(model, parameter_values=parameter_values)
    sim.solve([0, 3600])  # Simulate for 1 hour
    return {
        "time": sim.solution["Time [s]"].entries.tolist(),
        "voltage": sim.solution["Terminal voltage [V]"].entries.tolist(),
        "capacity": sim.solution["Capacity [Ah]"].entries.tolist()
    }

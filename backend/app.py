# backend/app.py
from fastapi import FastAPI, HTTPException
from backend.battery_simulation import run_simulation
from backend.data_pipeline import calculate_metrics
from backend.database import save_simulation, get_results

app = FastAPI()

@app.post("/simulate")
async def simulate(battery_model: str, parameters: dict):
    results = run_simulation(battery_model, parameters)
    metrics = calculate_metrics(results)
    simulation_id = await save_simulation(battery_model, parameters, metrics)
    return {"id": simulation_id, "metrics": metrics}

@app.get("/results")
async def get_results(battery_model: str = None):
    return await get_results(battery_model)

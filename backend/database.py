# backend/database.py
from tortoise.models import Model
from tortoise import fields

class Simulation(Model):
    id = fields.IntField(pk=True)
    battery_model = fields.CharField(max_length=255)
    parameters = fields.JSONField()
    metrics = fields.JSONField()
    created_at = fields.DatetimeField(auto_now_add=True)

async def save_simulation(battery_model, parameters, metrics):
    sim = await Simulation.create(
        battery_model=battery_model,
        parameters=parameters,
        metrics=metrics
    )
    return sim.id

async def get_results(battery_model=None):
    query = Simulation.all()
    if battery_model:
        query = query.filter(battery_model=battery_model)
    return await query

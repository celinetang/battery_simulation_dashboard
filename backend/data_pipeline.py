# backend/data_pipeline.py
import pandas as pd

def calculate_metrics(simulation_results):
    df = pd.DataFrame(simulation_results)
    df['state_of_health'] = df['capacity'] / df['capacity'].max()
    df['efficiency'] = (df['voltage'].mean() / df['voltage'].max()) * 100
    return df

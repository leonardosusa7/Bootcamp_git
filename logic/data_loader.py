import pandas as pd

def load_data(activities_path, health_path, users_path):
    """Carga los datasets de actividades, salud y usuarios."""
    activities = pd.read_csv(activities_path)
    health = pd.read_csv(health_path)
    users = pd.read_csv(users_path)
    return activities, health, users
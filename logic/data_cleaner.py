import pandas as pd
import numpy as np

def normalize_activities(activities: pd.DataFrame) -> pd.DataFrame:
    """Normaliza las actividades y agrega columnas faltantes."""
    activities['activity_type'] = activities['activity_type'].str.strip().replace({
        'Play': 'Playing',
        'Rest': 'Resting',
        'Walk': 'Walking'
    })
    activities['issue'] = np.nan
    activities['resolution'] = np.nan
    activities['duration_minutes'] = activities['duration_minutes'].replace('-', np.nan)
    return activities

def format_health(health: pd.DataFrame) -> pd.DataFrame:
    """Estandariza el formato del dataset de salud."""
    health['activity_type'] = 'Health'
    health['duration_minutes'] = 0
    health = health.rename(columns={'visit_date': 'date'})
    return health

def combine_data(activities: pd.DataFrame, health: pd.DataFrame) -> pd.DataFrame:
    """Combina actividades y salud."""
    return pd.concat([activities, health], ignore_index=True)

def merge_with_users(combined: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    """Une los datos combinados con la información de usuarios."""
    return combined.merge(users, on='pet_id', how='left')

def clean_final_df(final_df: pd.DataFrame) -> pd.DataFrame:
    """Convierte tipos de datos y ordena columnas."""
    final_df['pet_id'] = final_df['pet_id'].astype(int)
    final_df['date'] = pd.to_datetime(final_df['date'])
    final_df['activity_type'] = final_df['activity_type'].str.strip()
    final_df['duration_minutes'] = pd.to_numeric(final_df['duration_minutes'], errors='coerce').astype(float)
    final_df['issue'] = final_df['issue'].astype(str).str.strip()
    final_df['resolution'] = final_df['resolution'].astype(str).str.strip()
    final_df['owner_id'] = final_df['owner_id'].astype(int)
    final_df['owner_age_group'] = final_df['owner_age_group'].astype(str).str.strip()
    final_df['pet_type'] = final_df['pet_type'].astype(str).str.strip()

    cols = [
        'pet_id', 'date', 'activity_type', 'duration_minutes',
        'issue', 'resolution', 'owner_id', 'owner_age_group', 'pet_type'
    ]
    return final_df[cols]
from data_loader import load_data
from data_cleaner import (
    normalize_activities,
    format_health,
    combine_data,
    merge_with_users,
    clean_final_df
)

def all_pet_data(activities_pet, health_pet, users_pet):
    """Ejecuta el pipeline completo de integración de datos de mascotas."""
    
    # 1️⃣ Cargar datos
    activities, health, users = load_data(activities_pet, health_pet, users_pet)

    # 2️⃣ Transformar
    activities = normalize_activities(activities)
    health = format_health(health)
    
    # 3️⃣ Combinar
    combined = combine_data(activities, health)
    merged = merge_with_users(combined, users)
    
    # 4️⃣ Limpiar y devolver
    final_df = clean_final_df(merged)
    return final_df

if __name__ == "__main__":
    # Ejemplo de uso
    df = all_pet_data(
        "Data\pet_activities.csv",
        "Data\pet_health.csv",
        "Data\users.csv"
    )
    print(df.head())
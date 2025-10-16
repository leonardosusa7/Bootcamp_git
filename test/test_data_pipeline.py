import pandas as pd
from modules.data_pipeline import all_pet_data

def test_all_pet_data_structure():
    """
    Verifica que la función all_pet_data() combine y limpie correctamente los datos.
    """
    # Rutas a los CSV (ajusta si están en otra carpeta)
    activities_path = "Data/pet_activities.csv"
    health_path = "Data/pet_health.csv"
    users_path = "Data/users.csv"

    # Ejecutar la función
    df = all_pet_data(activities_path, health_path, users_path)

    # --- Pruebas ---
    # 1️⃣ Verificar tipo de salida
    assert isinstance(df, pd.DataFrame), "❌ El resultado no es un DataFrame"

    # 2️⃣ Columnas esperadas
    expected_columns = [
        "pet_id", "date", "activity_type", "duration_minutes",
        "issue", "resolution", "owner_id", "owner_age_group", "pet_type"
    ]
    assert list(df.columns) == expected_columns, "❌ Las columnas no coinciden con lo esperado"

    # 3️⃣ Verificar que pet_id no tenga nulos
    assert df["pet_id"].notnull().all(), "❌ Hay valores nulos en 'pet_id'"

    # 4️⃣ Verificar tipo de datos
    assert pd.api.types.is_datetime64_any_dtype(df["date"]), "❌ 'date' no es tipo datetime"

    # 5️⃣ owner_id debe ser entero
    assert pd.api.types.is_integer_dtype(df["owner_id"]), "❌ 'owner_id' no es tipo entero"

    print("✅ Todas las pruebas pasaron correctamente")

if __name__ == "__main__":
    test_all_pet_data_structure()
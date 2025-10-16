import logging
from modules.data_loader import load_data
from modules.data_cleaner import clean_data
from modules.data_merger import merge_data

# 🔧 Configurar logging
import pandas as pd

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            logging.warning(f"El archivo {file_path} está vacío. Se omite la carga.")
            return None
        return df
    except Exception as e:
        logging.error(f"Error al cargar el archivo {file_path}: {e}")
        return None

logging.basicConfig(
    level=logging.INFO,  # Nivel de detalle del log
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pet_data.log", mode="w", encoding="utf-8"),  # Archivo donde se guardan los logs
        logging.StreamHandler()  # También muestra los mensajes en la consola
    ]
)

def all_pet_data(activities_pet, health_pet, users_pet):
    """
    Combina, limpia y unifica los datos de actividades, salud y usuarios de mascotas.
    """
    logging.info("=== Inicio del proceso de integración de datos ===")

    try:
        # 1️⃣ Cargar datos
        logging.info("Cargando archivos CSV...")
        activities, health, users = load_data(activities_pet, health_pet, users_pet)
        logging.info("Archivos cargados correctamente.")

        # 2️⃣ Limpiar datos
        logging.info("Iniciando limpieza y normalización de datos...")
        activities, health = clean_data(activities, health)
        logging.info("Limpieza completada.")

        # 3️⃣ Unir datos
        logging.info("Uniendo datos de actividades, salud y usuarios...")
        final_df = merge_data(activities, health, users)
        logging.info("Datos combinados exitosamente.")

        logging.info("=== Proceso completado sin errores ===")
        return final_df

    except Exception as e:
        logging.error(f"Ocurrió un error durante el proceso: {e}")
        raise
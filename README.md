# Bootcamp_git# 🐾 Pet Data Integration Pipeline

Este proyecto implementa un **pipeline de integración y limpieza de datos de mascotas**, combinando información de actividades, salud y usuarios.  
Forma parte del ejercicio del curso **Bootcamp Git**, demostrando el uso correcto de Git, control de versiones, ramas, pruebas, issues y logs.

---

## 📂 Estructura del repositorio

Bootcamp_git/
│
├── Data/
│ ├── pet_activities.csv
│ ├── pet_health.csv
│ └── users.csv
│
├── logs/
│ └── pet_data.log
│
├── src/
│ ├── init.py
│ └── data_pipeline.py
│
├── tests/
│ └── test_data_pipeline.py
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── main.py

yaml
Copiar código

---

## 🚀 Descripción del Proyecto

El objetivo del proyecto es integrar y limpiar datos de diferentes fuentes (`activities`, `health`, `users`), generando un **DataFrame final consolidado**.  
El proceso incluye:
- Normalización de tipos de actividad  
- Manejo de valores faltantes  
- Unión de datos de salud y actividades  
- Conversión de tipos de datos  
- Validación con pruebas unitarias  
- Registro de eventos mediante logging  

---

## ⚙️ Instalación y Ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/<tu_usuario>/Bootcamp_git.git
   cd Bootcamp_git
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
Ejecutar el pipeline:

bash
Copiar código
python main.py
Revisar logs:
Los registros se guardan automáticamente en:

bash
Copiar código
logs/pet_data.log
🧪 Pruebas
El archivo tests/test_data_pipeline.py valida la función principal all_pet_data().

Ejecutar pruebas:

bash
Copiar código
pytest
🐞 Issues y Mejoras
#3 Error al cargar CSV vacío:
Se agregó manejo de advertencias en el log cuando los archivos CSV están vacíos (cerrado con commit close #3).

🏷️ Versionado
Versión estable actual: v1.0.0
Marcada con tag:

bash
Copiar código
git tag -a v1.0.0 -m "Versión estable inicial del pipeline de integración de datos con logging y validación de CSV vacío"
🧰 Tecnologías utilizadas
Python 3.10+

pandas – manipulación de datos

numpy – operaciones numéricas

pytest – pruebas automatizadas

logging – registro de eventos
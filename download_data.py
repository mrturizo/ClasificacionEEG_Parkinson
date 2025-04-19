
"""
Descarga y configuración de datos EEG desde OpenNeuro en formato BIDS.
"""

import os
import openneuro
from mne.datasets import sample

# Descargar datos de muestra de MNE si aún no están
print("🔍 Verificando datos de muestra MNE...")
sample.data_path()  # Esto se guarda en ~/.mne automáticamente

# Configuración de dataset de OpenNeuro
dataset = "ds002778"  # ID del dataset
bids_root = os.path.join(os.getcwd(), dataset)

# Descarga si no existen
if not os.path.isdir(bids_root):
    print(f"⏳ Descargando datos del dataset {dataset} desde OpenNeuro...")
    openneuro.download(dataset=dataset, target_dir=bids_root)
    print("✅ Descarga completada.")
else:
    print("📁 Los datos ya están disponibles en:", bids_root)

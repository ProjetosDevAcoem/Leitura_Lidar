import csv
from netCDF4 import Dataset
import numpy as np

# Abre o arquivo NetCDF
ds = Dataset("WLS200s-44_2025-10-01_14-02-36_ppi_34_50m.nc", "r")

# Seleciona o grupo
grp = ds.groups['Sweep_34889']

# Lê as variáveis
timestamps = grp.variables['timestamp'][:]
ranges = grp.variables['range'][:]
relative_beta = grp.variables['relative_beta'][:]
rotation_direction = grp.variables['rotation_direction'][:]

# Ordena pelo timestamp
ordem = np.argsort(timestamps)

timestamps_ordenados = timestamps[ordem]
ranges_ordenados = ranges[ordem]
relative_beta_ordenados = relative_beta[ordem]

# Salva no CSV
with open("saiu.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "range", "relative_beta", "rotation_direction"])  # cabeçalho
    
    for t, r, b in zip(timestamps_ordenados, ranges_ordenados, relative_beta_ordenados):
        writer.writerow([t, r, b])

print("Arquivo salvo como saida.csv (ordenado por timestamp)")

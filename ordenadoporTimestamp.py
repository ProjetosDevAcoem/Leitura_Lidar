import os
import csv
import netCDF4 as nc
import numpy as np

pasta = "src/"

# Lista todos os arquivos/subpastas
nomes = os.listdir(pasta)

for nome in nomes:
    caminho = os.path.join(pasta, nome)  # monta o caminho completo
    print("Abrindo arquivo:", caminho)

    # Abre o arquivo NetCDF
    ds = nc.Dataset(caminho, "r")

    # Agora você pode acessar os grupos, variáveis etc.
    # print(ds.groups.keys())        

    # Pega o nome do grupo que começa com "Sweep_"
    sweep_name = [g for g in ds.groups.keys() if g.startswith("Sweep_")][0]

    # Acessa o grupo dinamicamente
    grp = ds.groups[sweep_name]

    # Agora você pode acessar a variável
    relative_beta = grp.variables["relative_beta"][:]

    print(relative_beta)


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

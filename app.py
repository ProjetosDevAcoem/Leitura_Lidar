import csv
import netCDF4 as nc

fn = 'WLS200s-44_2025-09-22_00-00-06_ppi_34_50m.nc'
ds = nc.Dataset(fn)

# Mostra grupos e variáveis que podem ser acessadas dentro do arquivo
# print(ds)
# Mostra variáveis dentro do grupo
# print(ds.variables['relative_beta'])

#  =============================================
# Pega dados por grupos
grp = ds.groups['Sweep_27326']
print(grp)
# var = grp.variables['gate_index']

# print(var[:])
#  =============================================


# print(ds.__dict__)

# for var in ds.variables.values():
#     print(var)

# for dim in ds.dimensions.values():
#     print(dim)

#  =============================================
# Listar variáveis dentro do grupo
# print(grp.variables.keys())
#  =============================================

# var = grp.variables['range']
# print(var[:])

#  =============================================
# Extrai os dados
# data = var[:]

# # Salva em CSV
# with open("saida.csv", "w", newline="") as f:
#     writer = csv.writer(f)
    
#     # Se for 1D, salva linha por linha
#     if data.ndim == 1:
#         for val in data:
#             writer.writerow([val])
    
#     # Se for 2D ou maior, salva linha por linha
#     else:
#         for row in data:
#             writer.writerow(row)

# print("Arquivo salvo como saida.csv")
#  =============================================
 
#  =============================================
# Puxa valores de latitude e longitude do lidar
# for var in ds.variables.values():
#     print(ds['latitude'][:])
#  =============================================


# Comando para buscar o relative beta sem ter que acrescentar nenhum valor ao grupo Sweep:

# # Pega o nome do grupo que começa com "Sweep_"
# sweep_name = [g for g in ds.groups.keys() if g.startswith("Sweep_")][0]

# # Acessa o grupo dinamicamente
# sweep_group = ds.groups[sweep_name]

# # Agora você pode acessar a variável
# relative_beta = sweep_group.variables["relative_beta"][:]

# print(relative_beta)

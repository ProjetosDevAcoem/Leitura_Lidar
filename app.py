import csv
import netCDF4 as nc

fn = 'WLS200s-44_2025-10-01_14-02-36_ppi_34_50m.nc'
ds = nc.Dataset(fn)

# Testar conexão com arquivo
# print(ds)

#  =============================================
# Pega dados por grupos
grp = ds.groups['Sweep_34889']

var = grp.variables['gate_index']

print(var[:])
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
#     print(ds['Sweep_34889'][:])
#  =============================================
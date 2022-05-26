"""
Recebe uma distância e a velocidade de movimentação, e retorna as horas que seriam gastas para percorrer em linha reta.
"""
print("Horas para percorrer distância:")

# Entrada
distancia = float(input("Distância (km): "))
velocidade = float(input("Velocidade (km/h): "))

# Processamento
horas = distancia / velocidade
minutos = horas * 60
h, m = divmod(minutos, 60)

# Saída
print(f"Tempo de viagem: {round(horas,2)} horas.")
print(f"Tempo de viagem: {int(h)}h{int(m)}m.")

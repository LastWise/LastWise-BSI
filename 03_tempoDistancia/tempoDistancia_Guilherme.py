# Entrada
distância = float(input("Digite a distância em km: "))
velocidade_média = float(input("Digite a velocidade média em km/h: "))

# Processamento
tempo = distância / velocidade_média

# Saída
print(f"O tempo estimado é de {tempo} horas.")

# Processamento
# Opcional: imprimir o tempo em horas, minutos e segundos
tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
horas = int(tempo_s / 3600)  # parte inteira
tempo_s = int(tempo_s % 3600)  # o resto
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)

# Saída
print(f"{horas}h{minutos}m{segundos}s")
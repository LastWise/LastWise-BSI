from totalSegundos import totalSegundos

def main():
    print("Dias para segundos")

    # Entrada de Dados
    dias = int(input("Dias: "))
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    # Processamento
    totalsegundos = totalSegundos(dias, horas, minutos, segundos)

    # Saída
    print(f"{dias}d{horas}h{minutos}m{segundos}s => {totalsegundos} segundos")

if __name__ == "__main__":
    main()





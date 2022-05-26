print("Aumento Salarial")

# Entrada
salario = float(input("Salário: "))
percentualAumento = float(input("Percentual de Aumento: "))

# Processamento
valorAumento = salario * percentualAumento / 100
novoSalario = salario + valorAumento

# Saída
print(f"\nNovo Salário: R$ {novoSalario}")
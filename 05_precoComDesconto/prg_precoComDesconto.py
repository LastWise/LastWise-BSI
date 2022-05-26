print("Preço Com Desconto")

# Entrada
preço = float(input("Preço do produto: "))
percentualDesconto = float(input("Percentual de desconto: "))

# Processamento
valorDesconto = preço * percentualDesconto / 100
novoPreço = preço - valorDesconto

# Saída
print(f"Preço com desconto: R$ {novoPreço}")
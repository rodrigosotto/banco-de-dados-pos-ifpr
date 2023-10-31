from datetime import datetime
print (datetime.now())

idade = 30
print('Minha idade é',idade, 'anos')

# Criando um array com 100 posições e nomes de carros
carros = ["Carro " + str(i) for i in range(1, 101)]

# Imprimindo os nomes dos carros
for carro in carros:
    print(carro)

print("Lista de carros impares:")
# Pegando apenas os carros em posições ímpares usando uma compreensão de lista
carros_impares = [carros[i] for i in range(0, len(carros), 2)]

# Imprimindo os carros em posições ímpares
for carro in carros_impares:
    print(carro)

idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)

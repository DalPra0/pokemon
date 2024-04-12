numeros = [5, 7, 12, 2, 9, 21]

print(numeros)
print("")
numero_certo = sorted(numeros)
print(numero_certo)
print("")

for i in range(len(numeros)):
    print(numeros[i])

for i in range(len(numero_certo)):
    print(numero_certo[i])

numeros[1] = 17
numeros[3] = 22
print(f"Novo vetor {numeros}")
numeros[2] = 1
numeros[4] = 29
print(f"Novo vetor {numeros}")

for i in range(len(numeros)):
    print(numeros[i])

print("")

print(numeros[5] + numeros[4])
print(numeros[3] - numeros[1])
print(numeros[0] * numeros[5])
print(numeros[3] / numeros[2])


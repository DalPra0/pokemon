menor = -1
contador = 0
numero = int(input("Informe um numero: "))
menor = numero

while contador <= 3:
    numero = int(input("Informe um numero: "))
    if numero < menor:
        menor = numero
    else:
        menor = menor
        
    contador += 1

print("O menor numero digitado foi: ", menor)
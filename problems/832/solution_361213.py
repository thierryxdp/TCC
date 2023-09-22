def eh_quadrada(matriz):
    matriz = []

while True:

tamanho = int(input())

valor = 1

if tamanho == 0:

break

for i in range(tamanho):
linha = []
  for j in range(tamanho):
    linha.append(valor)
    valor = valor*2
     if len(linha)==tamanho:

    valor = linha[0]

    valor = valor*2

matriz.append(linha)

tamanho_caracter=(str(matriz[-1][-1]))

tamanho_caracter=len(tamanho_caracter)

aux=tamanho_caracter+1

for a in matriz:

for b in a:
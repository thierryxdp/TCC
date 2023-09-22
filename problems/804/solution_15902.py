def filtra_pares():
    tupla2 = ([])
tupla = ([])
valor = 0
for p in range(1,5):
    valor = int(input("Digite 4 numeros inteiros:"))
    tupla2.append(valor)
    if valor %2 == 0:
        tupla.append(valor)
return (f'Numeros digitados:{tupla2}')(f'Pares digitados:{tupla}')
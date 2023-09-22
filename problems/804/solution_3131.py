filtra_pares = (int(input('digite um numero: ')),
                int(input('digite um numero: ')),
                int(input('digite um numero: ')),
                int(input('digite um numero: ')))
for n in filtra_pares:
    if n % 2 == 0:
        print(n, end=' ')
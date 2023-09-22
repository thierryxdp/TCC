def maiores(lis, n):
    maiores_numeros = list()
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
    return maiores_numeros


valores = list(map(int, input('Digite os valores da lista: ').split()))
num = int(input('Desejas retornar os números a partir de qual valor? '))

print(maiores(valores, num))
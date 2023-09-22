def maiores(lista,n):
    'Funcao que dada uma lista de numeros int e um numero n int, retorna outra lista com todos os numeros maiores que n de forma crescente'
    'int,int=>int'
    maiores=list()
    lista.sort()
    for x in lista:
        if x>=n:
            maiores.append(x)
        return maiores
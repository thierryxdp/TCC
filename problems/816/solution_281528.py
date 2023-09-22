def maiores(lista,n):
    ''' Função que recebe uma lista e um número inteiro "n", e retorna outra lista
    contendo os números maiores que "n" ordenados de forma crescente'''
    #Casos de teste
    ''' maiores([1,2,4,545,76],2) -> [4, 76, 545]
    maiores([1,3,2,500,700],2) -> [3, 500, 700]
    maiores([100,30,56,98,1500],40) -> [56, 98, 100, 1500]'''
    list(lista)
    lista.append(n)
    lista.sort()
    indiceN = lista.index(n)
    if n not in lista:
        lista.append(n)
    return lista[indiceN+1:]
def maiores(lista,n):
    ''' Dada uma lista de número inteiros e um número 
    inteiro n, retorna outra lista, que contenha todos
    os números maiores que n, em ordem crescente
    list, int -> list'''
    ListaF = []
    for j in lista range(lista):
        if j > n:
            L = ListaF.append(j)
            L.sort()
            return L
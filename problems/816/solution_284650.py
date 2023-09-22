def maiores(lista,n):
    ''' Dada uma lista de número inteiros e um número 
    inteiro n, retorna outra lista, que contenha todos
    os números maiores que n, em ordem crescente
    list, int -> list'''
    listaF = []
    for j in lista:
        if j>n:
            ListaF.append(j)
            ListaF.sort()
            return ListaF
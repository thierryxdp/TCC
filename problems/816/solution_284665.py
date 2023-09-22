def maiores(lista,n):
    ''' Dada uma lista de número inteiros e um número 
    inteiro n, retorna outra lista, que contenha todos
    os números maiores que n, em ordem crescente
    list, int -> list'''
    ListaF = []
    for i in range(len(lista)):
        if i > n:
            ListaF.append(i)
            ListaF.sort()
            return ListaF
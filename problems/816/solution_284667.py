def maiores(lista,n):
    ''' Dada uma lista de número inteiros e um número 
    inteiro n, retorna outra lista, que contenha todos
    os números maiores que n, em ordem crescente
    list, int -> list'''
    lista_final = []

    for elemento in lista:
        if elemento > n:
        lista_final.append(elemento)
        return lista_final
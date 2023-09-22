def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um numero inteiro n e retorna uma nova lista contendo os numeros maiores que n da lista de entrada ordenados em ordem crescente
    list, int -> list'''
    lista_saida=[]
    for numero in lista:
        if numero>n:
            list.append(lista_saida,numero)
            list.sort(lista_saida)
            return lista_saida
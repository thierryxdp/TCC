def insere(lista_numero,n):
    '''recebe uma lista em ordem crescente com números
    inteiros e um numero inteiro (n), na qual a função
    vai incluir n em uma posição de forma que a lista 
    se mantenha ordenada'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero
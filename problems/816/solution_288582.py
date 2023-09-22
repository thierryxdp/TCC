def maiores(lista, numero):
    '''funçao que dado uma lista de numeros e um numero separa da lista os maiores que o numero dado e os coloca em ordem crescente'''
    lista_maiores = []
    for elemento in lista:
        if elemento > numero:
            lista_maiores += [elemento]
    list.sort(lista_maiores)
    return lista_maiores
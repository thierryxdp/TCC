def maiores(lista, n):
    '''Função que, dado a lista de numeros inteiros e um numero inteiro n,
    retorna outra lista que contém os numeros da primeira lista maiores que
    n'''
    # Cria lista vazia
    lista_maiores = list()

    # Para cada nÃºmero da lista
    for num in lista:
        # Se ele for maior que o numero n
        if num > n:
            # Adiciona-o Ã  lista de maiores
            lista_maiores.append(num)
            lista_maiores.sort()

    # Retorna a lista de maiores
    return lista_maiores
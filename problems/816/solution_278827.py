def maiores(lista, n):
    '''Função que, dada lista de numeros inteiros e um numero inteiro n,
    retorna outra lista de inteiro que contenha os valores da lista original
    que são menosres que n'''
    # Cria lista vazia
    lista_maiores = list()

    # Para cada numero da lista
    for num in lista:
        # Se ele for maior que o numero n
        if num > n:
            # Adiciona  lista de maiores
            lista_maiores.append(num)

    # Retorna a lista de maiores
    return lista_maiores
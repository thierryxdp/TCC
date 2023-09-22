def maiores(lista, n):
    # Cria lista vazia
    lista_maiores = list()

    # Para cada nÃºmero da lista
    for num in lista:
        # Se ele for maior que o numero n
        if num > n:
            # Adiciona-o Ã  lista de maiores
            lista_maiores.sort(num)

    # Retorna a lista de maiores
    return lista_maiores
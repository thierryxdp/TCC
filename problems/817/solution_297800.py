def acima_da_media(lista):
    """
        Função que recebe uma lista de notas e retorna uma nova lista contendo apenas as notas que ficaram acima da média (7).
        (1) A variável acima_media recebe da lista de entrada todas as notas acima da média.

        list --> list
        
    """
    
    acima_media = []
    for i in lista:
        if i > 5:
            acima_media.append(i)
    acima_media.sort()
    return acima_media
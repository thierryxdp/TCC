def acima_da_media(lista):
    '''Função que cria uma lista com notas acima da média dada as notas de
    alunos de uma turma. Entrada é lista e int'''
    # Calcula media da lista de notas
    media = sum(lista)/len(lista)

    # Cria lista vazia
    acima = list()

    # Para cada nota na lista
    for nota in lista:
        # Se a nota e maior que a media
        if nota > media:
            # Adiciona na lista de notas acima da media
            acima.append(nota)

    # Ordena a lista de notas acima da media
    acima.sort()

    # Retorna a lista de notas acima da media
    return acima
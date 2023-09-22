def acima_da_media(lista_notas):
    '''Funcao que recebe uma lista com a nota
    de cada aluno de uma turma, e retorna uma 
    nova lista ordenada com as notas que ficaram
    acima da media.
    Dados de entrada: list
    Valor de saida: list
    '''
    soma_das_notas = sum(lista_notas)
    media_das_notas = (soma_das_notas/(len(lista_notas)))
    lista_notas_acima_da_media = []
    for i in lista_notas:
        if i > media_das_notas:
            list.append(lista_notas_acima_da_media,i)
            list.sort(lista_notas_acima_da_media)
    return lista_notas_acima_da_media
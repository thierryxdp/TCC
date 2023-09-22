def acima_da_media(lista):
    """Função que recebe uma lista com notas de alunos de uma turma,
    retornando uma lista ordenada com as notas acima da media
    entrada: lista
    retorno: lista"""
    lista_nota= list()
    media= sum(lista)/len(lista)
    for elemento in lista:
        if elemento > media:
            lista_nota.append(elemento)
    lista_nota.sort()
    return lista_nota
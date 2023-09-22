def acima_da_media(lista):
    """Função que recebe uma lista com notas de alunos de uma turma,
    retornando uma lista ordenada com as notas acima da media
    entrada: lista
    retorno: lista"""
    lista=list()
    for elemento in lista_numeros:
        if elemento > 7:
            lista.append(elemento)
    lista.sort()
    return lista
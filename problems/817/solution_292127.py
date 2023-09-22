def acima_da_media(lista):
    """
    list->list
    :param lista: Recebe lista com as notas de todos os alunos de uma turma
    return: Retorna lista ordenada dos alunos que tiveram nota acima da média
    """
    listaMaior = []
    media=(sum(lista)/len(lista))
    for el in lista:
        if el > media:
            listaMaior.append(el)
    listaOrdenada=sorted(listaMaior)
    return listaOrdena
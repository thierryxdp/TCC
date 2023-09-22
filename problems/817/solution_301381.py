def acima_da_media(lista):
    """
    funcao que dada uma lista com as notas dos alunos de uma 
    turma, retorna uma lista ordenada com as notas que ficaram
    acima da média.
    :param lista_notas: list
    :return: list 
    """
    m = sum(lista)//len(lista)
    lista.append(m)
    ordenada = sorted(lista)
    indice_media = ordenada.index(m)
    nova = ordenada[indice_media + 1:].copy()

    if m in nova:
        del nova[0]

    return nova
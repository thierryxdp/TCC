def acima_da_media(lista_n):
    """
    Função que dada uma lista com as notas dos alunos de uma turma,
    retorne uma lista ordenada com as notas que ficam acima da media.
    Parametro de Entrada: list
    Valor de Saida: list
    """
    soma=sum(lista_n)
    numero_elemen=len(lista_n)
    media=soma//numero_elemen
    list.append(lista_n,media)
    list.sort(lista_n)
    return lista_n[1+list.index(lista_n,media):]
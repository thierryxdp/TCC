def acima_da_media(lista):
    """Função acima_da_media que dada uma lista com as notas dos
    alunos de uma turma, retorne uma lista ordenada com as notas
    que ficaram acima da média.
    lista -> lista
    """
    soma_notas = sum(lista)
    qtd_notas = len(lista)
    media = soma_notas/qtd_notas
    media1 = [media]
    lista2 = lista + media1
    lista2.sort()
    x = lista2.index(media)
    y = lista2[x+1:]
    return y
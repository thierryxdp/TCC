def acima_da_media (lista = list) -> list:
    """Função que recebe uma lista de números inteiros com as notas dos alunos de uma turma (lista)
    e retorna uma lista ordenada com as notas que ficaram acima da média."""
    x = len(lista)
    media = float(sum(lista)/x)
    if media in lista:
        lista = sorted(lista)
        indice = lista.index(media)
        return lista[indice+1:]
    else:
        lista = lista + [media]
        lista = sorted(lista)
        indice = lista.index(media)
        return lista[indice+1:]
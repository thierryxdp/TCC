def acima_da_media (lista = list) -> list:
    """Função que recebe uma lista de números inteiros com as notas dos alunos de uma turma (lista)
    e retorna uma lista ordenada com as notas que ficaram acima da média."""
    x = len(lista)
    media = round(sum(lista)/x)
    lista = sorted(lista)
    y >= media
    indice = list.index(lista, y)
    return lista[indice+1:]
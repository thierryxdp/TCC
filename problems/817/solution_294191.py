def acima_da_media (lista = list) -> list:
    """Função que recebe uma lista com as notas dos alunos de uma turma (lista) e retorna uma lista
    ordenada com as notas que ficaram acima da média."""
    x = len(lista)
    media = sum(lista)/x
    nova_lista = sorted(lista)
    nova_lista = nova_lista[media+1:]
    return nova_lista
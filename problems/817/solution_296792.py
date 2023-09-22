def maiores(lista, n):
    '''Retorna uma lista com os números maiores que o n dado. List, Int -> List'''
    if n not in lista:
    list.insert(lista, 1, n)
    list.sort(lista)
    Posicao_n = list.index(lista, n)
    NovaLista = lista[Posicao_n + 1:]
    return NovaLista

def acima_da_media(nota):
    '''Dado uma lista com as notas dos alunos, retorna uma lista com as notas acima da média. List, Int->List'''
    n = sum(nota)/len(nota)
    return maiores(nota, n)
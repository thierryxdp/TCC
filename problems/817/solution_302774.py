def maiores(lista,n):
    """Função que recebe uma lista e um número "n", e retorna uma lista com todos os número da primeira maiores que "n" e "n" e a organiza. list -> list"""
    l = []
    for i in range(len(lista)):
        if lista[i] > n:
            l.append(lista[i])
    l.sort()
    return l

def acima_da_media(notas):
    """Função que dadas as notas dos alunos, retorna uma lista ordenada com as notas dos que ficaram acima da média. st -> list"""
    notas_media =[]
    media = sum(notas)/len(notas)
    for i in range (len(notas)):
        if notas[i] > media:
            notas_media.append(notas[i])
    notas_media.sort()
    return notas_media
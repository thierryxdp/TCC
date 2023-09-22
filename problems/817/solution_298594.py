def maiores(lista,n):
    maiores = list()
    for x in lista:
        if x >= n:
            maiores.append(x)
    return maiores

def acima_da_media(notas):
    """ Insira uma lista coom as notas dos alunos e a função retornara uma lista ordenada das
    notas acima da media"""
    media = sum(notas)/len(notas)
    acima_media = maiores (notas,media)
    return acima_media
def acima_da_media(notas):
    """funçao que dada uma lista com as notas dos alunos, retorna uma lista ordenada com as notas que ficaram acima da media
    list -> list"""
    a= sum(notas)/len(notas)
    lista = notas+[a]
    list.sort(lista)
    x= list.index(lista,a)
    y= list.count(lista,a)
    return lista[x+y:]
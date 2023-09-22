def acima_da_media(notas):
    """função que retorna as notas dos alunos acima da media.
    list->list"""
    import math
    media=math.ceil(sum(notas)/len(notas))
    list.sort(notas)
    x= list.index(notas,media)
    del notas[:x]
    if x not in notas:
        return del notas[:x+1]
    else:
        return notas
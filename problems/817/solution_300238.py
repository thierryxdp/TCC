def acima_da_media(notas):
    """função que retorna as notas dos alunos acima da media.
    list->list"""
    import math
    media=math.ceil(sum(notas)/len(notas))
    list.sort(notas)
    x= list.index(notas,media)
    if x not in notas:
        del notas[:x+1]
    if x not in notas:
        del notas[:x+2]
        return notas
    else:
        del notas[:x]
        return notas
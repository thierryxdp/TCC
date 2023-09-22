def acima_da_media(notas):
    """função que retorna as notas dos alunos acima da media.
    list->list"""
    import math
    a= len(notas)
    media=math.ceil(sum(notas)/len(notas))
    list.append(notas,media)
    list.sort(notas)
    x= list.index(notas,media)
    del notas[:x+1]
    if a==0:
        return []
    else:
        return notas
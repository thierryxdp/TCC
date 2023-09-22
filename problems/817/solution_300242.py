def acima_da_media(notas):
    """função que retorna as notas dos alunos acima da media.
    list->list"""
    import math
    media=math.ceil(sum(notas)/len(notas))
    list.sort(notas)
    list.append(notas,media)
    x= list.index(notas,media)
    del notas[:x]
    return notas
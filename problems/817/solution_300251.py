def acima_da_media(notas):
    """função que retorna as notas dos alunos acima da media.
    list->list"""
    import math
    media=math.ceil(sum(notas)/len(notas))
    list.append(notas,media)
    list.sort(notas)
    x= list.index(notas,media)
    
    if len(notas)==1:
        return []
    else:
        del notas[:x+1]
        return notas
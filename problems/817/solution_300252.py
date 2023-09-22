def acima_da_media(notas):
    """função que retorna as notas dos alunos acima da media.
    list->list"""
    import math
    a= len(notas)
    media=math.ceil(sum(notas)/len(notas))
    list.append(notas,media)
    list.sort(notas)
    x= list.index(notas,media)
    
    if a==1:
        return []
    else:
        del notas[:x+1]
        return notas
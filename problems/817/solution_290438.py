def acima_da_media(notas):
    """retorna uma lista com as notas que ficaram acima da média
    list->list"""
    a=sum(notas)
    b=len(notas)
    c=a//b
    list.sort(notas)
    if list.count(notas,c)>=1:
        d=list.index(notas,c)
        return notas[d+1:]
    else:
        list.append(notas,c)
        list.sort(notas)
        e=list.index(notas,c)
        return notas[e+1:]
def acima_da_media(ls):
    """
    retorna uma lista com as notas maiores ou iguais a 5
    """
    y=0
    for t in ls:
        y=y+t
    y=y/len(ls)
    i=[]
    for x in ls:
        if x>y:
            i=i+[x]
    i=sorted(i)
    return i
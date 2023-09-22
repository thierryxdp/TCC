def acima_da_media(ls):
    """
    retorna uma lista com as notas maiores ou iguais a 5
    """
    i=[]
    for x in ls:
        if x>=5:
            i=i+[x]
            return i
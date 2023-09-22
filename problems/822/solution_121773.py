def repetidos(lista):
    """coment"""
    i=0
    s=0
    while i<len(lista):
        if lista[i+1]==lista[i]:
            s+=1
            i+=1
        return s
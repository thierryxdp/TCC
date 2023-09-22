def repetidos(lista):
    """coment"""
    i=0
    s=0
    while i<len(lista):
        if lista[i]==lista[i+1]:
            s+=1
            i+=1
    return s
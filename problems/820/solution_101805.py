def posLetra (texto, letra, numero):
    lista=[texto]
    p=0
    newlista=[]
    
    while p<len(texto):
        if texto[p] == letra:
            newlista=newlista+[p]
        p=p+1
    if len (newlista) < numero:
        return -1
    return newlista
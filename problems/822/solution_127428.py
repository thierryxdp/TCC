def repetidos(lista):
    i=0
    r=0
    
    while i<len(lista)+1:
        if i==i+1:
            r=r+1
        i=i+1
    return r
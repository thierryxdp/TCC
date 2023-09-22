def repetidos(lista):
    c=0
    num=0
    tam=len(lista)
    
    while c<tam:
        if c>0 and lista[c]==lista[c-1]:
            num += 1
            
        c += 1
        
    return num
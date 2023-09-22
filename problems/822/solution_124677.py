def repetidos(lista):
    i = 0
    x = 0
    if lista[1]==lista[0]:
        x=1
    i = 1    
    while i < len(lista):
     if lista[i] == lista[i-1]:
        x+=1
    
     i+=1
    return x
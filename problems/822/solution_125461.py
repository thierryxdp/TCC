def repetidos (lista):
    ''' devolve a quantidade de vogais presentes no texto.
    str --> int'''
    
    i=0
    l = []
    lista.sort()
    rep=0 
    
    for i in range(0,len(lista)-2):
        if (lista[i]==lista[i+1]):
            rep =rep +  1
    return rep
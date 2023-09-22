def repetidos (lista):
    ''' devolve a quantidade de vogais presentes no texto.
    str --> int'''
    
    i=0
    l = []
    
    for i in lista:
        if i in l:
            l.append(i)
    l.sort()
    return l
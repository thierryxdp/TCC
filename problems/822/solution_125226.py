def repetidos(lista):
    i=0
    repeticoes = 0
    
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            repeticoes = repeticoes + 1
        i = i+1
    return repeticoes
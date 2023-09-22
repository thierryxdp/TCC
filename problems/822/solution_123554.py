def repetidos(lista):
    Q = len(lista)
    i = 0
    repeticoes = 0
    
    while i < Q:
        if lista[i-1] == lista[i]:
            repeticoes = repeticoes + 1
        i = i +1
        
    return repeticoes
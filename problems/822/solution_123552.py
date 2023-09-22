def repetidos(lista):
    Q = len(lista)
    i = i + 1
    repeticoes = 0
    
    while i < Q:
        if lista[i] == lista[i+1]:
            repeticoes = repeticoes + 1
        i = i +1
        
    return repeticoes
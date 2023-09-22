def repetidos(lista):
    i = 0
    score = 0
    while i<len(lista):
        if lista[i] == lista[i+1]:
            score = score + 1
        
        i = i + 1
    return score
def repetidos(lista):
    i = 0
    score = 0
    while i<len(lista):
        if lista[i] == lista[i+1]:
            if lista[i+1]> len(lista):
                score = score + 0
            else:
            score = score + 1
        i = i + 1
    return score
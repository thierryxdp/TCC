def repetidos(lista):
    i = 1
    score = 0
    while i<len(lista):
        if lista[i-1] == lista[i]:
            score = score + 1 
            '''if lista[i+1]> len(lista):
                score = score + 0
            else:
            	score = score + 1'''
        i = i + 1
    return score
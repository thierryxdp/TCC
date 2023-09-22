def repetidos(lista):
    qnt=0
    i=1
    
    while i < len(lista):
        if lista[i]==lista[i+1]:
                qnt = qnt + 1
        i=i-1
    return qnt
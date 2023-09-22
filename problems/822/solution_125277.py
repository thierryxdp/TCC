def repetidos(lista):
    qnt=0
    i=0
    while i < len(lista):
        if lista[i]==lista[i+1]:
            qnt = qnt + 1
        i=i+1
    return qnt
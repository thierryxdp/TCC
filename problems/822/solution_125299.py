def repetidos(lista):
    qnt=0
    i=1
    while i < len(lista):
        if lista[i]==lista[-1+i]:
            qnt = qnt + 1
        i=i-1
    return qnt
def repetidos2(lista):
    i=0
    quantidade=0
    while i<len(lista):
        if lista.count(i)>1:
          quantidade=quantidade+1
        i=i+1
    return quantidade
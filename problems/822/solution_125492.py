def repetidos(lista):
    i=0
    quantidade=0
    while i<len(lista):
        if lista.count(i)>1:
          quantidade=quantidade+1
        elif lista.count(i)>3:
            quantidade=quantidade+1
        elif lista.count(i)>3:
            return quantidade=quantidade+1
        i=i+1
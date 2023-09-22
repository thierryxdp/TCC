def repetidos(lista):
    i=0
    r=[]
    while i < len(lista):
        if lista[i]==lista[i-1]:
            r=r+(lista[i])
        else:
            i=i+1
    return len(r)
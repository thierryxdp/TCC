def repetidos(lista):
    i=0
    numero=[]
    while i< len(lista):
        i=i+1
        numero=lista.count(numero[i])
    return numero
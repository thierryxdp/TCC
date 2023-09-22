def repetidos(lista):
    i=0
    numero=[]
    while i<len(lista):
        numero=numero.count(lista[i])
    return numero
def repetidos(lista):
    i=0
    numero=[]
    while i<len(lista):
        numero=numero+(lista[i],)
        numero.count(lista[i])
    return numero
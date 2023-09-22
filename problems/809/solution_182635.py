def intercala(lista1, lista2):  
    lista=[]
    for i in len(lista1):
        lista.append(lista1[i-1])+lista2[i]
    return lista
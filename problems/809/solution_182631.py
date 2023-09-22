def intercala(lista1, lista2):  
    lista=[]
    for i in len(lista1):
        lista.append(i)+lista2[i]
    return lista
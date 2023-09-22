def intercala(lista1, lista2):  
    lista=[]
    for i in range(lista1):
        lista.append(i)+lista2[i]
    return lista
def intercala(lista1, lista2):  
    lista=[]
    for i in lista1:
        lista.append(i)+lista2[i-1]
    return lista
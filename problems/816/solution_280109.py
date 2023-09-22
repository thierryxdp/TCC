def maiores(lista,x):
    
    lista.append(x)
    lista1=list.sort(lista)
    lista2=list.index(lista1,x)
   
    return lista[lista2+1:]
def maiores(lista,x):
    
    
    lista1=list.insert(lista,1,x)
    lista2=list.sort(lista1)
    lista3=list.index(lista2,x)
   
    return lista[lista3+1:]
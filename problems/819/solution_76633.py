def filtraMultiplos(lista,n):
    "Retorna todos os elementos da listaque forem divisiveis por n. list,int->list"
    i=0
    listadiv = []
    pega = 0
    
    while int(lista)%n==0:
        pega = list.pop(lista,[i])
        list.append(listadiv, pega)
        i+=1
    return listadiv
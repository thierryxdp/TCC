def filtraMultiplos(lista,n):
    "Retorna todos os elementos da listaque forem divisiveis por n. list,int->list"
    i=0
    listadiv = 0
    pega = list.pop(lista,0)
    while pega%n==0:
        list.append(listadiv, pega)
        i+=1
    return listadiv
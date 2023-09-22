def filtraMultiplos(lista,n):
    "Retorna uma lista com todos os elementos divisíveis por n. list,int->list"
    sep = str.split(lista, " ")
    i = 0
    
    while sep%0==0:
        list.insert(lista,sep)
        i+=1
    return lista
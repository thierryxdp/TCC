filtraMultiplos(listaBelha):
    
    listaNueba = []
    ind = 0
    while ind<len(listaBelha):
        if listaBelha[ind]%2 == 0:
            listaNueba =  listaNueba + listaBelha[ind]
        ind = ind + 1  
        
    return listaNueba
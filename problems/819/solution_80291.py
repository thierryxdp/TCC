def filtraMultiplos(listaBelha,n):
    '''função que filtra os numeros multiplos de um numero N'''
    listaNueba = list()
    ind = 0
    while ind<len(listaBelha):
        if listaBelha[ind]%n == 0:
            
            listaNueba.append(listaBelha[ind])
        ind = ind + 1  
        
    return listaNueba
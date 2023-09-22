def faltante(lista):
    lst_return = []    
    
    for i in range(len(lista) - 1): 
        if lista[i + 1] != lista[i] + 1 :
            lst_return.append(lista[i] + 1)
            
    return lst_return
def filtro(lista, n):
    newList = []
    cont = 0
    
    while(cont < len(lista)):
        if lista[cont] % n == 0:
            newList.append(lista[cont])
            
        cont = cont + 1
            
    
    return newList
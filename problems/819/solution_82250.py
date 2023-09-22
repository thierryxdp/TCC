def filtraMultiplos(lista_numeros,n):
    "função que filtra os múltiplos de um numero n"
    "list, int -> list"
    listavazia = list()
    ind = 0
    while ind<len(lista_numeros):
        if lista_numeros[ind]%n == 0:
            
            lista_vazia.append(lista_numeros[ind])
        ind = ind + 1  
        
    return lista_vazia
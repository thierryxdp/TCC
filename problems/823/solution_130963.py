def faltante(lista):
    tam= len(lista)
    lista_o = list(range(1, tam+1))
    i=0
    
    while i<len(lista):
        
        if lista_o[i] not in lista:
            return lista[i]
        elif lista_o == lista:
            return len(lista)+1
            
        i = i + 1
            
    return 0
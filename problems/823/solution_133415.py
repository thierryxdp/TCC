def faltante(lista):
    
    """Dada uma lista com numeros 
    inteiros diferentes, retorna 
    os numeros pertencentes ao 
    intervalo entre 1 e N. list -> int """
    

    lst_return = []    
        
    if lista[0] != 0:
        lst_return.append(list(range(0, lista[0])))
    
            
    return lst_return
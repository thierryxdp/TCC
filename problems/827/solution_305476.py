def qtd_divisores(n):
    """Funcao que conta quantos divisores o numero de entrada possui;
    int -> int"""
    
    i = 1
    listadedivisores = 0
    ultimonumero = n+1
    lista = list(range(1,10))
    
    while i< len(lista):
        if n/i == 0:
            listadedivisores += 1
        i += 1
        
    return listadedivisores
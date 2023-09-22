def qtd_disores(n):
    """Funcao que conta quantos divisores o numero de entrada possui;
    int -> int"""
    
    i = 1
    listadedivisores = 0
    ultimonumero = n+1
    
    while i<ultimonumero:
        if n/i == 0:
            listadedivisores += 1
        i += 1
        
    return len(listadedivisores)
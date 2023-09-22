def qtd_divisores(n):
    """Funcao que conta quantos divisores o numero de entrada possui;
    int -> int"""
    
    i = 1
    divisores = 0
    ultimonumero = n+2
    lista = list(range(1,ultimonumero))
    
    while i < len(lista):
        if n%i == 0:
            divisores += 1
        i += 1
        
    return divisores
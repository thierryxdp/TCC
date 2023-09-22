def concatenacao(a, b):
    """Junta duas strings na forma 'abba'
    
    string + string + string + string --> string
    
    Casos de teste:
    concatenacao('aba', 'ba') == 'abababaaba'
    concatenacao('bonito', 'feio') == 'bonitofeiofeiobonito'
    concatenacao('esquerda', 'direita') == 
    'esquerdadireitadireitaesquerda'
    """
    return str(a) + str(b) + str(b) + str(a)
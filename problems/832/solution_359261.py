def eh_quadrada(matriz): 
    """Identifica e retorna verdadeiro caso uma matriz 
    seja quadrada e falso caso não seja; 
    list -> bool"""
    a = len(matriz)
    b = len(matriz[0]) 
    if a == b or a == 0 : 
        return True 
    else : 
        return False
def eh_quadrada(matriz): 
    """Identifica e retorna verdadeiro caso uma matriz 
    seja quadrada e falso caso não seja; 
    list -> bool"""
    a = len(matriz)
    if a==0 : 
        return True 
    elif a != 0 and a == len(matriz[0]) : 
        return True
    else : 
        return False
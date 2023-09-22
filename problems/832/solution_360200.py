def eh_quadrada(m):
    
    "matriz"
    if len(m) == len(m[0]):
        return True 
    elif len(m) != len(m[0]):
        return False 
    elif m==[]:
        return True
def eh_quadrada(M):
    if len(M) == 0:
        return True 
    elif len(M) == len(M[0]):
        return True
    else:
        return False
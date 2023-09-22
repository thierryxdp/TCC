def eh_quadrada(m,n):
    matriz=[[m],[n]]
    '''	Função booleana que identiffica se uma matriz é quadrada'''
    if len(matriz)==0 :
        return []
    if matriz==[]:
        return True 
    elif m==n:
        return True 
    else:
        return False
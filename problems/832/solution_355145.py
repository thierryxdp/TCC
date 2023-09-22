def eh_quadrada(matriz):
    '''eh_quadrada recebe um lista e devolve True ou False
    determine se a matriz é quadratica ou não e retorne true ou false, respectivamente 
    list(list) --> bool'''
    
    if matriz==[]:
        return
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False
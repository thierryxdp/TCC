def eh_quadrada(matriz):
    """Cálculo de uma função booleana para identificar se uma matriz é quadrada ou não.
    
       Parameters:
       matriz: matriz a ser analisada 
       
       Returns:
       Retorna se a matriz é quadrada ou não,, dado que:
       list -> bool 
    """
    nlinhas= len(matriz)
    ncolunas= range(len(matriz[0]))
    if nlinhas == ncolunas:
        return True
    elif nlinhas==0 and ncolunas==0:
        return True
    else:
        return False
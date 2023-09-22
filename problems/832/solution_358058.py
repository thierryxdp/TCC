def eh_quadrada(matriz):
    """Cálculo de uma função booleana para identificar se uma matriz é quadrada ou não.
    
       Parameters:
       matriz: matriz a ser analisada 
       
       Returns:
       Retorna se a matriz é quadrada ou não,, dado que:
       list -> bool 
    """
    nlinhas= len(matriz)
    ncolunas= len(matriz[0])
    if nlinhas == ncolunas:
        return True
    else:
        return False
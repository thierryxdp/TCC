def eh_quadrada(matriz):
    """Cálculo de uma função booleana para identificar se uma matriz é quadrada ou não.
    
       Parameters:
       matriz: matriz a ser analisada 
       
       Returns:
       Retorna se a matriz é quadrada ou não,, dado que:
       list -> bool 
    """
    if len(matriz) == len(matriz[0]):
        return True
    else:
        False
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
    if nlinhas != ncolunas:
        return False
    for i in range(0,nlinhas):
        for j in range(0,ncolunas):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
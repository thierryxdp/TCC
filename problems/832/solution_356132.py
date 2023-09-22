def eh_quadrada(matriz):
    """Retorna se uma matriz é quadrada; lista -> bool."""
    for i in range(0, (len(matriz)+1)):
        if len(matriz)==len(matriz[i]):
            j= True
        else:
            j= False
    return j
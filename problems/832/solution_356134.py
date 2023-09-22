def eh_quadrada(matriz):
    """Retorna se uma matriz é quadrada; lista -> bool."""
    for i in range(0, (len(matriz))):
        for j in range(0, (len(matriz[i]))):
            if len(matriz)==len(matriz[i]):
                k= True
            else:
                k= False
    return k
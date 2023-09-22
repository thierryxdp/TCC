def eh_quadrada(matriz=[]): 
    if len(matriz)==[]: 
        return (True) 
    linha=len(matriz) 
    coluna=len(matriz[0])
    if linha==coluna:
        return (True)
    else:
        return (False)
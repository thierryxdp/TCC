def eh_quadrada (matriz):
    """Função que identifica se a matriz fornecida é quadrada. Retorna True
    em caso positivo e False em caso negativo."""
    """list-->bool"""
    ind=0
    if len(matriz)==0:
        return True
    for j in matriz:
        if len(matriz[ind])==len(matriz):
            resultado=True
            ind+=1
        else:
            resultado=False
    
    return resultado
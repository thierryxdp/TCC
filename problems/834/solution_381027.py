def media_matriz (matriz):
    """Retorna cada elemento da matriz de entrada divido ao meio"""
    soma=[]
    for lista in matriz:
        for elemento in lista:
            soma.append(elemento)
    return sum(soma)/2
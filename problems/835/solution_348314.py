def melhor_volta(matriz):
    """
"""
    num=0
    lista=[]
    for num in range(len(matriz)):
        lista.append(min(matriz[num]))
        
    return lista.index(min(lista))
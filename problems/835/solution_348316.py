def melhor_volta(matriz):
    """
"""
    num=0
    lista=[]
    corrida=[]
    for num in range(len(matriz)):
        lista.append(min(matriz[num]))
    for num in range(len(matriz)):
        corrida.append(min(matriz[num]))
        
    return corrida
    #lista.index(min(lista))
def melhor_volta(matriz):
    """
"""
    num=0
    lista=[]
    corrida=[]
    
    for num in range(len(matriz)):
        lista.append(min(matriz[num]))
        
    for num in range(len(matriz)):
        corrida.append(matriz[num].index(min(matriz[num]))+1)
        
        
    return corrida
    #lista.index(min(lista))
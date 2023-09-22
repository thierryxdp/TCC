def eh_quadrada(matriz):
    """ Funcao bool que diz se matriz eh quadrada ou nao"""
    linha=[]
    coluna=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            linha=len(matriz)
            coluna=len(matriz[0])
            if linha==coluna:
                return True
            else: 
                return False
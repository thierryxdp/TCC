def eh_quadrada (matriz):
    '''Dada a função, identifique e retorne se a matriz
        é quadrada;
        list -> bool'''
    componentes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            componentes = componentes+1
    if lwn(matriz)==0:
        return True
    elif (componentes/len(matriz)== len(matriz):
          return True
     else:
          return False
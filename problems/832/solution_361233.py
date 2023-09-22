def eh_quadrada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if len(matriz) == len(matriz[0]):
                   return True
            elif len(matriz[0]) == []:
                   return True
            else:
                   return False
def eh_quadrada(matriz):
    i = 0
    if len(matriz) == 0:
        return True

    for j in matriz:
         if len(j) == len(matriz):
             i += 1
         if i == len(matriz): 
             return True
         else:
             return False
def eh_quadrada(matriz):
  
    elementos=0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elementos= elementos+1
    if len(matriz)==0:
        return True
    elif (elementos/len(matriz))== len(matriz):
        return True
    else:
        return False
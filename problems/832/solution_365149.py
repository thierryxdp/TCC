#Matriz Quadrada
def eh_quadrada(matriz):
    #Função para identificar se uma matriz é quadrada; List => Bolean
    for i in range(len(matriz)):
        if len (matriz[i]) != len(matriz):
            return False
    return True
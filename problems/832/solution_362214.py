def eh_quadrada(matriz):
    ''' Essa função recebe uma matriz e identifica se ela 
    eh quadrada ou não. Caso seja, retorna o valor booleano 
    True, caso não, retorna False.
    Obs.: uma matriz vazia é considerada quadrada.
    matriz (int) -> bool'''
    if matriz == []:
        return True #eh quadrada
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False # n eh quadrada

#Casos de teste
# eh_quadrada([]) == True

# matriz = [[2,2,2],[2,2,2],[2,2,2]]
# eh_quadrada(matriz) == True

# matriz = [[1,2],[3,4],[5,6]]
# eh_quadrada(matriz) == False

# matriz = [[10,12],[32,5],[7,6],[-3,2]]
# eh_quadrada(matriz) == False

# matriz = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
# eh_quadrada(matriz) == True
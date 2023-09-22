def conta_numero (numero,matriz):
    '''retorna quantas vezes o num do 1 arg e encontrado
    dentro da matriz do 2 arg
    int , list(list) -> int'''
    
    conta = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                conta += 1
    return conta
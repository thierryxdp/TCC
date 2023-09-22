def eh_quadrada(matriz):
    '''
    Funçao que dado uma matriz, identifica se ela é quadrada ou não.
    OBS: Matriz vazia tambem é considerada quadrada
    list(list) -> bool
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if len(matriz) == len(matriz[i]) or len(matriz[i]) == 0:
                return True
            else:
                return False
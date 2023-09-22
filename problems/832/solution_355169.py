def eh_quadrada(matriz):
    """uma função booleana chamada
para identificar se uma matriz é quadrada.
Obs: uma matriz vazia (sem nenhuma linha
nem coluna) é considerada quadrada."""
    nlin = len(matriz)#qnt de linha
    
    if nlin == 0: #se linha igual a 0, então não tem matriz
        return True
    
    elif len(matriz[0]) == nlin: # se qnt de coluna e qnt linha forem iguais, é uma matriz quadrada
        return True
    
    elif len(matriz[0][0]) == 0:
        return False

    else: #caso não esteja dentro do parametros, retorna False
        return False
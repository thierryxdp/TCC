def eh_quadrada(matriz):
    if len(matriz) == 0:
        return True
    elif len(matriz[0]) == len(matriz):
        return True
    else:
        return False
    
# Primeiro definimos a função pedida passando como parâmetro, uma matriz qualquer.
# Dentro da função, fazemos duas verificações, a primeira, é se é uma matriz vazia e
# a segunda é se o número de linhas é igual ao número de colunas. Caso alguma das
# duas verificações seja atendida, a função retorna True, já que teríamos uma matriz
# quadrada, caso contrário, retorna False
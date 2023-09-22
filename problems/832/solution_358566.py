def eh_quadrada(matriz):
    """ funcao que recebe uma matriz e identifica se ela é quadrada.retorna a resposta em booleano.
    entrada->list(list)
    saida->bool"""
    if matriz==[]:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else: return False
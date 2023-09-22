#Start your python function here
def filtra_pares(x):
    '''filtra_pares recebe uma tupla e devolve uma tupla
    determina o valor de uma tupla
    tupla --> tupla'''
    resposta = []
    if x[0]%2 == 0:
        resposta.append(x[0])
    if x[1]%2 == 0:
        resposta.append(x[1])
    if x[2]%2 == 0:
        resposta.append(x[2])
    if x[3]%2 == 0:
        resposta.append(x[3])
    return tuple(resposta)
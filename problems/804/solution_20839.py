#Start your python function here
def filtra_pares(x1, x2, x3, x4):
    '''a'''
    resposta = ()
    if (x1%2) == 0:
        resposta = resposta + (x1,)
    if (x2%2) ==0:
        resposta = resposta + (x2,)
    if (x3%2) == 0:
        resposta = resposta + (x3,)
    if (x4%2) == 0:
        resposta = resposta + (x4,)
    else:
        resposta = resposta
    return resposta
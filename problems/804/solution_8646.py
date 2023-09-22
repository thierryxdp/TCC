#Start your python function here
def filtra_pares(tupla):
    if(tupla[0]%2 == 0):
        resposta += (tupla[0],)
    if(tupla[1]%2 == 0):
        resposta += (tupla[1],)
    if(tupla[2]%2 == 0):
        resposta += (tupla[2],)
    if(tupla[3]%2 == 0):
        resposta += (tupla[3],)
    return resposta
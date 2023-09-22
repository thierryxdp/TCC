def filtra_pares(tupla):
    '''Função que retorna os elementos pares de uma tupla
    valor de saída e entrada: tupla'''
    resposta = ()
    if tupla[0] % 2 == 0:
        resposta = resposta + (tupla[0],)
    if tupla[1] % 2 == 0:
        resposta = resposta + (tupla[1],)
    if tupla[2] % 2 == 0:
         resposta = resposta + (tupla[2],)
    if tupla[3] % 2 == 0:
         resposta = resposta + (tupla[3],)
    return resposta
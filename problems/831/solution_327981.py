def lingua_p(palavra):
    ''' Função que traduz uma palavra do português para a língua do p
    str -> str '''
    resposta = ''
    for x in palavra:
        if str.upper(x) in "AEIOUÃÕÁÉÍÓÚÂÊÎÔÛ":
            resposta = resposta + x+"p"+x
        else:
            resposta = resposta + x
    return resposta
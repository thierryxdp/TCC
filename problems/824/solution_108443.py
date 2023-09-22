def uppCons(frase):
    '''Função que se recebida uma frase retorna todas as consoantes desta,
    em letra maiúscula e os demais caracteres. str -> str'''
    n = 0
    while n < len(frase):
        if frase[n] in 'QWRTPSDFGHJKLÇZXCVBNMqwrtpsdfghjklçzxcvbnm':
            str.upper(frase[n])
            frase = frase + str.upper(frase[n])
        n = n + 1
    return frase
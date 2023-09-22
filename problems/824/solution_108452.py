def uppCons(frase):
    '''Função que se recebida uma frase retorna todas as consoantes desta,
    em letra maiúscula e os demais caracteres. str -> str'''
    frase_nova = ' '
    n = 0
    while n < len(frase):
        if frase[n] in 'QWRTPSDFGHJKLÇZXCVBNMqwrtpsdfghjklçzxcvbnm':
            frase_nova = str.upeer(frase[n])
        n = n + 1
    return frase_nova
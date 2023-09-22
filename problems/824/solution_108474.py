def uppCons(frase):
    '''Função que se recebida uma frase retorna todas as consoantes desta,
    em letra maiúscula e os demais caracteres. str -> str'''
    frase_nova = ' '
    n = 0
    while n < len(frase):
        if frase[n] in 'QWRTPSDFGHJKLÇZXCVBNMqwrtpsdfghjklçzxcvbnm':
            frase_nova = frase_nova + frase[n]
            frase_nova = str.upper(frase_nova)
            str.replace(frase, frase[n], frase_nova)
        n = n + 1
    return frase
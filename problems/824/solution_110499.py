uppCons f(frase):
    '''dada uma frase, retorna esse frase com todas as consoantes em maiúsculas;
    str --> str'''
    i = 0
    novaFrase = ''
    while i < len(frase):     
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            novaFrase = novaFrase + str.upper(frase[i])
        else:
            novaFrase = novaFrase + frase[i]
        i = i + 1
    return novaFrase
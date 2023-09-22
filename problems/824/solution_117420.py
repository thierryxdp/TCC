def uppCons(texto):
    '''
    Função converte as consoantes de uma frase em maiúsculo
    str -> str
    '''
    i = 0
    saida = ''
    while i < len(texto):
        if texto[i] in 'bcçdfghjklmnpqrstvwwyz':
            saida = saida + str.upper(texto[i])
                
        else:
            saida = saida + texto[i]

        i += 1
    
    return saida
lingua_p(p):
    '''Função que dado uma palavra como entrada, retorna a mesma palavra traduzida para a lingua do p.
    str -> str'''
    traduzida = ''
    p = str.lower(palavra)
    x = 'qwrtypsdfghjklçzxcvbnm'
    for i in range(len(p)):
        if p[i] not in x:
            traduzida += p[i] + 'p' + p[i]
        else:
            traduzida = palavra[i]
    return traduzida
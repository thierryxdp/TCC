def lingua_p(palavra):
    '''Função que dado uma palavra como entrada, retorna a mesma palavra traduzida para a lingua do p.
    str -> str'''
    traduzida = ''
    palavra = str.lower(palavra)
    x = 'qwrtypsdfghjklçzxcvbnm'
    for i in range(len(palavra)):
        if palavra[i] not in x:
            traduzida += palavra[i] + 'p' + palavra[i]
        else:
            traduzida += palavra[i]
    return traduzida
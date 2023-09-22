def lingua_p(palavra):
    '''função que recebe como parâmetro uma palavra(em português) e retorna
    a mesma palavra traduzida para a língua do P. str -> str'''
    traducao = ''
    palavra = str.lower(palavra)
    restricao = 'qwrtypsdfghjklçzxcvbnm'
    for i in range(len(palavra)):
        if palavra[i] not in restricao:
            traducao += palavra[i] + 'p' + palavra[i]
        else:
            traducao += palavra[i]
    return traducao
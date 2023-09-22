def lingua_p(palavra):
    '''função que dado-lhe uma string de entrada sendo uma palavra em português verifica e retorna esta mesma palavra traduzida para a língua do P. 
    str-> str'''
    tradu = ''
    palavra = str.lower(palavra)
    restricao = 'qwrtypsdfghjklçzxcvbnm'
    for i in range(len(palavra)):
        if palavra[i] not in restricao:
            tradu += palavra[i] + 'p' + palavra[i]
        else:
            tradu += palavra[i]
    return tradu
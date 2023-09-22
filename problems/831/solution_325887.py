def lingua_p(palavra):
    ''' Função que recebe uma palavra em português e retorna esta mesma palavra
    traduzida para a língua do P.
    str-->str'''
    linguap = ''
    for i in range(len(palavra)):
        if palavra[i] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' :
            linguap = linguap + palavra[i]
        else:
            linguap = linguap + palavra[i] + 'p' + palavra[i]
    return linguap
def lingua_p (palavra):
    '''
    Retorna a palavra na lingua do p
    string -> string
    '''
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    linguadop = ''
    for posicao in range(len(palavra)):
        if palavra[posicao] in vogais:
            linguadop = linguadop + palavra[posicao] + 'p' + palavra[posicao]
        else:
            linguadop = linguadop + palavra[posicao]
    return linguadop
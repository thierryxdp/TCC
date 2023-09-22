def lingua_p (palavra):
    '''
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            vogais = vogais + 'p' + vogais
        palavra = traducao + palavra + vogais
    return palavra
def lingua_p (palavra):
    '''
    palavra = traducao + palavra + vogais
    return palavra
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            vogais = vogais + 'p' + vogais
    return vogais
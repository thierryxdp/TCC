def lingua_p (palavra):
    '''
    vogais = vogais + 'p' + vogais
    palavra = traducao + palavra + vogais
    return palavra
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            traducao = traducao + 'p' + vogais
    return traducao
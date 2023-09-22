def lingua_p (palavra):
    '''
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            vogais = vogais + 'p' 
        palavra = traducao + palavra + vogais
    return palavra
def lingua_p(palavra):
    '''
    '''
    traducao= ''
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            traducao= traducao+vogais+'p'+vogais
    return traducao
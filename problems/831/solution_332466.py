def lingua_p(palavra):
    '''
    '''
    traducao= ''
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            traducao= traducao+vogais[0]+'p'+vogais[0]
    return traducao
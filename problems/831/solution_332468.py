def lingua_p(palavra):
    '''
    '''
    traducao= ''
    for vogais in range(palavra):
        if vogais in 'AEIOUaeiou':
            traducao= traducao+vogais[0]+'p'+vogais[0]
    return traducao
def lingua_p(palavra):
    '''
    '''
    traducao= ''
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            traducao= traducao+vogais[vogais]+'p'+vogais[vogais]
    return traducao
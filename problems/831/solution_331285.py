def lingua_p(palavra):
    '''...'''
    
    p = ''
    
    for i in palavra:
        if i in 'AEIOUaeiouÁÉÍÓÚáéíóú':
            p = p + i + 'p' + i
        else:
            p = p + i
    return p
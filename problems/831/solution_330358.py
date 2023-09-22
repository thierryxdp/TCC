def lingua_p (palavra):
    
    ''' Função que traduz uma dada palavra para a 
        língua do P.
        str -> str '''
    
    plvr_final = ''
    
    for letra in palavra: 
        if letra in 'AEIOUaeiouÁÉÍÓÚáéíóú':
            plvr_final = plvr_final + letra + 'p' + letra
        else:
            plvr_final = plvr_final + letra 
    
    return plvr_final
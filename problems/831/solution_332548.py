def lingua_p (palavra):
    '''
    
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiouáéíóú':
            traducao = traducao + vogais + 'p' + vogais
    for consoantes in palavra :
        if consoantes in 'bcdfghjklmnpqrstuvwxyzç':
            traducao = traducao + consoantes 
    return traducao
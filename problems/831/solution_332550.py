def lingua_p (palavra):
    '''
    for consoantes in palavra :
        if consoantes in 'bcdfghjklmnpqrstuvwxyzç':
            traducao = traducao + consoantes 
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiouáéíóú':
            traducao = traducao + vogais + 'p' + vogais
    return traducao
def lingua_p (palavra):
    '''
   
    '''
    vogais = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiouáéíóú':
            vogais = vogais + 'p' + vogais
    for consoantes in palavra :
        if consoantes in 'bcdfghjklmnpqrstuvwxyzç':
            consoante = consoantes 
    return vogais
def lingua_p (palavra):
    '''
   
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiouáéíóú':
            vogais = vogais + 'p' + vogais
    for consoantes in palavra :
        if consoantes in 'bcdfghjklmnpqrstuvwxyzç':
            consoantes = consoantes 
    return vogais + consoantes
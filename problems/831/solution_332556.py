def lingua_p (palavra):
    '''
   
    '''
    resposta = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiouáéíóú':
            vogais1 = vogais + 'p' + vogais
    for consoantes in palavra :
        if consoantes in 'bcdfghjklmnpqrstuvwxyzç':
            consoante1 = consoantes 
    return vogais1 + consoante1
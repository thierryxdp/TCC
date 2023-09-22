def lingua_p (palavra):
    '''
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            traducao = traducao + vogais + 'p' + vogais
    for consoantes in 'bcdfghjklmnpqrstuvwxyzç':
    
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            traducao = traducao + vogais + 'p' + vogais
    for consoantes in palavra :
        if consoantes in 'bcdfghjklmnpqrstuvwxyzç':
            traducao = traducao + consoantes 
    return traducao
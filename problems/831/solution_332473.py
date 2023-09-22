def lingua_p (palavra):
    '''
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            traducao = traducao + vogais + 'p' + vogais
    for consoantes in 'bcdfghjklmnpqrstuvwxyzç':
    
    '''
    traducao = ""
    consoantes = 'bcdfghjklmnpqrstuvwxyzç'
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            traducao = traducao + vogais + 'p' + vogais
    return traducao + consoantes
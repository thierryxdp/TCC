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
            vogais = vogais + 'p' + vogais
    for consoantes in palavra 'bcdfghjklmnpqrstuvwxyzç':
        consoantes = consoantes
    traducao = traducao + vogais + consoantes
    return traducao
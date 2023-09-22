def lingua_p (palavra):
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            traducao = traducao + vogais + 'p' + vogais
    for consoantes in 'bcdfghjklmnpqrstuvwxyzç':'''
    
    '''
    traducao = ""
    for vogais in palavra:
        if vogais in 'AEIOUaeiou':
            vogais = traducao + vogais + 'p' + vogais
    for consoantes in 'bcdfghjklmnpqrstuvwxyzç':
        consoantes = traducao + consoantes
    traducao = vogais + consoantes
    return traducao
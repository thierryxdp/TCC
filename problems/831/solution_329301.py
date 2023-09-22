def lingua_p (palavra):
    '''
    '''
    palavra_min = palavra.lower()
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    palavra_p = ''
    
    for letra in palavra_min:
        palavra_p = palavra_p.index(letra)
        if letra not in consoantes:
            palavra_p = palavra_p.index('p') + letra
    return palavra_p
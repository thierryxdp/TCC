def lingua_p (palavra):
    ''' dada uma palavra, retorna a mesma palavra traduzida
        para a lingua do P.
    '''
    palavra_min = palavra.lower()
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    palavra_p = ''
    
    for letra in palavra_min:
        palavra_p = palavra_p + letra
        if letra not in consoantes:
            palavra_p = palavra_p + 'p' + letra
    return palavra_p
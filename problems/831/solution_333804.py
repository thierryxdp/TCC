def lingua_(palavra):
    '''função que recebe palavra em portugues e retorna palavra traduzida em lingua do p.
    str--> str'''
    
    traduzido_p = []
    contador = 0
    
    for palavra in list(candelabro):
        if palavra in 'candelabro':
            traduzido_p.append(letra + 'p' + letra)
        else:
            traduzido_p.append(letra)
    return ''.join(traduzido_p)
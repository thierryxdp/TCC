def lingua_p(palavra):
    '''função que dada uma palavra retorna ela mesma traduzida pra lingua do P:str->str'''
    P = ''
    for x in palavra:
        if x in 'aeiouáãàâéêèiíîìóõôôúùù':
            P =P+x+'p'+x
        else x in 'bcdfghjklmnpqrstvwxyzç':
            P += x
    return str.lower(P)
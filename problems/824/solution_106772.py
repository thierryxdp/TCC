def uppCons(frase):
    '''retorna as consantes mauisculas, str->str'''
    vogais = 'aeiouáéíóúâêîôû'
    x= frase
    w=0
    while w<len(frase):
        if frase[w] not in vogais:
            w= w.replace(frase[w],frase[w].upper())
        w = w+1
    return x
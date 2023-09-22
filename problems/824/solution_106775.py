def uppCons(frase):
    '''retorna a frase com consoantes maisculas
    str->str'''
    vogais = 'AEIOUaeiouãâáàêéôóõíûúùÂÃÁÀÉÊÎÍÔÓÛÚ'
    x = frase
    y=0
    while y<len(frase):
        if frase[y] not in vogais:
            x= x.replace(frase[y],frase[y].upper())
        y = y+1
    return x
def uppCons(frase):
    '''retorna as consantes mauisculas, str->str'''
    vogais = 'AEIOUaeiouãâáàêéôóõíûúùÂÃÁÀÉÊÎÍÔÓÛÚ'
    a = frase
    i=0
    while i<len(frase):
        if frase[i] not in vogais:
            a= a.replace(frase[i],frase[i].upper())
        i = i+1
    return a
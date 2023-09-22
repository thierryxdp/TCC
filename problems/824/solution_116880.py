def uppCons(frase):
    '''retorna a entrada frase com as consonantes maiusculas
    str->str'''
    contador = 0
    novaFrase = ''
    while contador <= len(frase)-1:
        if frase[contador] in 'bcdfghjklmnpqrstvwxyzç':
            novaFrase = novaFrase+str.upper(Frase[contador])
        else:
            novaFrase = novaFrase+Frase[contador]
        contador=contador+1
    return novaFrase
def uppCons(frase):
    '''retorna uma string com as consoantes que apareceram em um texto,
    maiusculas
    consoantes=consoantes+frase[i]
        i=i+1
    str->str'''
    consoantes = ''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz' and 'AEIOUaeiou':   
            consoantes = str.upper(consoantes) + str.lowerfrase[i]    
        i=i+1
    return consoantes
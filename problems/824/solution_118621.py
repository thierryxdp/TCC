def uppCons(frase):
    '''retorna uma string com as consoantes que apareceram em um texto,
    maiusculas
    consoantes=consoantes+frase[i]
        i=i+1
    str->str'''
    i = 0
    consoantes=()
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':  
            consoantes = str.upper('bcdfghjklmnpqrstvwxyz') + frase[i]
        i=i+1
    return consoantes
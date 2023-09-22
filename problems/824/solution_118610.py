def uppCons(frase):
    '''retorna uma string com as consoantes que apareceram em um texto,
    maiusculas
    str->str'''
    i=0
    consoantes='bcdfghjklmnpqrstvwxyz'
    while i<len(frase):
        if frase[i] in consoantes:  
            consoantes = str.upper(consoantes) + frase[i]
        i=i+1         
        return consoantes
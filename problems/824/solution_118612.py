def uppCons(frase):
    '''retorna uma string com as consoantes que apareceram em um texto,
    maiusculas
    str->str'''
    i=0
    consoantes= ''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':  
            consoantes = str.upper(consoantes) in frase[i]
        i=i+1         
        return consoantes
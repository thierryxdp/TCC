def uppCons(frase):
    '''retorna uma string com as consoantes que apareceram em um texto,
    maiusculas
   str->str'''   
    consoantes = ''
    x = 1
    while x < len(frase):  
        if frase[x] in 'bcdfghjklmnpqrstvwxyz':
            consoantes = str.upper(consoantes) + frase[x]
        x = x + 1
    return  consoantes
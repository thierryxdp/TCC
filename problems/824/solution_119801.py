def  uppCons(frase):
    '''função em, que dada uma frase, retorna a frase com todas as 
    consoantes em maiúsculas (e os demais caracteres exatamente como estavam na frase original): strm -> str'''
    i=0
    letras=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklnmopqrstvwxyzç':
            letras = letras + str.upper(frase[i])
        else:
             letras=letras+frase[i][c]
        i=i+1
    return i
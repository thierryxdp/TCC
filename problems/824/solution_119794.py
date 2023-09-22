def  uppCons(frase):
    '''função em, que dada uma frase, retorna a frase com todas as 
    consoantes em maiúsculas (e os demais caracteres exatamente como estavam na frase original): strm -> str'''
    c=0
    i='
    while c<len(frase):
        if frase[c] in 'bcçdfghjklnmopqrstvwxyz':
            i+=str.upper(frase[c])
            else:
                i+=frase[c]
                c=c+1
                return i
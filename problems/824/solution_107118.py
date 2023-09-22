def uppCons(frase):
    ''' funcao que dado uma frase a retorna com suas consoantes maiusculas
    str->str'''
    s = ''
    x=0
    while x<len(frase):
        if frase[x] in 'bcdfghjklÇçmnpqrstvxwyz':
            s=s+frase[x].upper() 
        else: 
            s=s+frase[x]
        x=x+1
    return s
def uppCons(frase):
    '''retorna frase com consoantes maiusculas
    str->str'''
    i=0
    Texto=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
        	Texto=Texto+str.upper(frase[i])
        else:
            Texto=Texto+frase[i]
        i=i+1
    return Texto
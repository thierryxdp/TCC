def uppCons (frase):
    '''
    	Essa função recebe uma frase e retorna a mesma com todas as suas consoantes maiusculas e 
        suas demais caracteres são mantidos como estavam
        str->str
    '''
    i=0
    while i<len(frase):
        if frase[i] in ('bcdfghjklmnpqrstvwxyz'):
            str.upper frase[i]
            i=i+1
    return frase
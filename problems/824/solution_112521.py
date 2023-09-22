def uppCons (frase):
    '''
    	Essa função recebe uma frase e retorna a mesma com todas as suas consoantes maiusculas e 
        suas demais caracteres são mantidos como estavam
        str->str
    '''
    return ''.join(x.upper() if x in 'bcdfghjklmnpqrstvxwyz')
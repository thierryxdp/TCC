def uppCons (frase):
    '''
    	essa função recebe uma frase e retorna a mesma com suas consoantes em maiusculo
        e os caracteres demais são mandtidos da mesma forma
        str->str
    '''
    i=0
    while i < len(frase):
        if frase[i]  in 'bcdfghjklmnpqrstvwxyz':
            x = frase[i].upper()
            i = i + 1
    return frase
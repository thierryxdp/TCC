def uppCons(frase):
    '''Recebe uma frase e retorna a frase com suas
    consoantes em maisculas.
    string -> string'''
    i = 0
    l_frase = frase.split()
    while i < len(l_frase):    
    	if 'aeiou' not in frase:
            lista = []
            palavra = frase[i].upper()
            lista += [palavra]
            return lista
    
        i += 1
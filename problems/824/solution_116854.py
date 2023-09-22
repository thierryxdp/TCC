def uppCons(frase):
    '''
    	Funcao que recebe uma frase e retorna a frase com
        todas as suas consoantes em maiusculas e os demais
        caracteres exatamente como estavam na frase original
        str -> str
    '''
    i = 0
    letras = ''
    
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
        	letras.replace(frase, frase[i], frase[i].upper())
        else:
        	letras.replace(frase, frase[i], frase[i].lower())
    	i += 1
    return letras
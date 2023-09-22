def uppCons(frase):
    '''
    	Funcao que recebe uma frase e retorna a frase com
        todas as suas consoantes em maiusculas e os demais
        caracteres exatamente como estavam na frase original
        str -> str
    '''
    i = 0
    letras = []
    lista_frase = list(frase)
    
    while i < len(lista_frase):
        if lista_frase[i] in 'bcçdfghjklmnpqrstvwxyz':
        	letras.insert(i, lista_frase[i].upper())
        else:
        	letras.insert(i, lista_frase[i])
    	i += 1
    return str(''.join(letras))
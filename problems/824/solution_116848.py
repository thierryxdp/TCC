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
    
    if lista_frase[i] in 'aeiou':
        letras.insert(i, lista_frase[i].lower())
    i += 1
    while i < len(lista_frase):
        if lista_frase[i] in 'bcdfghjklmnpqrstvwxyz':
        	letras.insert(i, lista_frase[i].upper())
        i += 1
    return letras
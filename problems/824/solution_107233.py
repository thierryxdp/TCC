def uppCons(frase):
    '''Função que recebe como entrada uma frase e retorne a frase com todas
       as suas consuantes em maiúculas.
       str ---> str'''
    contador = 0
    resp = '' 
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstxyz':
            letra = str.upper(frase[contador])
            resp = resp + letra
        else:
            resp = resp + frase[contador]
        contador = contador + 1
	return resp
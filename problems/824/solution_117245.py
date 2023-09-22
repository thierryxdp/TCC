def uppCons(frase):
    '''Esta função recebe uma frase e retorna a mesma com
    todas as consoantes em letras maiúsculas
    string -> string'''
	lista_frase = list(frase)
	contador = 0
	letras = []
    
    while contador < len(lista_frase):
		if lista_frase[contador] in 'cbcdfghjklmnpqrstvwxyz':
def uppCons(frase):
    '''Dada uma frase como entrada, retorna a mesma com 
    todas as consoantes em letra maiuscula
    str -> str'''
    contador = 0
    frase_nova = ''
    while contador < len(frase):
        if frase[contador] not in 'AEIOUáéíóúaeiou':
            frase_nova = frase_nova + frase[contador].upper()
		else:
            frase_nova = frase_nova + frase[contador]
		contador +=1
	return frase_nova
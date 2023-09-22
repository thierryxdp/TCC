def uppCons(frase):
    '''Dada uma frase como entrada, retorna a mesma
    com todas as consoantes em letra maiuscula
    str -> str'''
    contador = 0
    while contador < len(frase):
        if frase(contador) not in 'AEIOUaeiou':
            frase(contador).upper()
		contador +=1
	return frase
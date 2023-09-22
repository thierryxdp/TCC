def uppCons(frase):
    '''função que recebe uma frase e a retorna com suas consoantes
    em maiúsculas'''
    contador = 0
    troca = ''
    resultado = frase.upper()
	if resultado[contador] != frase[contador] and frase[contador]=='a':
		resultado.replace(resultado[contador], 'a')
	elif resultado[contador] != frase[contador] and frase[contador]=='e':
		resultado.replace(resultado[contador], 'e')
	elif resultado[contador] != frase[contador] and frase[contador]=='i':
		resultado.replace(resultado[contador], 'i')
	elif resultado[contador] != frase[contador] and frase[contador]=='o':
		resultado.replace(resultado[contador], 'o')
	else: 
		resultado.replace(resultado[contador], 'u')
        contador = contador + 1
    return resultado
def uppCons(frase):
    '''função que recebe uma frase e a retorna com suas consoantes
    em maiúsculas'''
    contador = 0
    troca = ''
    resultado = frase[:]
    while contador < len(frase):
        troca = frase[contador]
        if frase[contador] not in 'aeiou':
            resultado.replace(resultado[contador], troca.upper())
        contador = contador + 1
    	return resultado
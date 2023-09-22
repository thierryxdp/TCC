def uppCons(frase):
    '''Função que retorna em maiúsculas, as consoantes de uma frase de entrada: str -> str'''
    
    indice = 0
    transformar = ''
    
    
	while indice < len(frase):
        if frase[indice] in 'bcçdfghjklmnpqrstvxwyz':
            transformar += str.upper(frase[indice]) #transformar = transformar + str.upper(frase[indice])
        else:
            transformar += frase[indice]
        indice += 1 #indice = indice + 1
        
    return transformar
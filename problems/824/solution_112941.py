def uppCons(frase):
    '''Função que recebe uma frase e retorna as consoantes em maiúsculo
    	e os demais caracteres como se encontravam'''
    i=0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i] = str.upper(frase)
        i = i + 1
    return frase
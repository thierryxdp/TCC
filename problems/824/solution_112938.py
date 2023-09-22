def uppCons(frase):
    '''Função que recebe uma frase e retorna as consoantes em maiúsculo
    	e os demais caracteres como se encontravam'''
    i=0
    s=''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            s = s + str.upper(frase[i])
        i = i + 1
    return s+frase
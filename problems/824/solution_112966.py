def uppCons(frase):
    '''Função que recebe uma frase e retorna as consoantes em maiúsculo
    	e os demais caracteres como se encontravam'''
    i=0
    lista = list(frase)
    while i<len(lista):
        if lista[i] not in 'AEIOUaeiou':
            lista[i] = str.upper(lista[i])
        i = i + 1
    str.replace(str.join('+',lista),'+','')
    return lista
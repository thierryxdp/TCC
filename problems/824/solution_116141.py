def uppCons(frase):
    '''Função que recebe uma frase e retorna as suas consoantes em 
    	maiúsculas e os demais caracteres como se encontravam
        
        str -> str'''
    i=0
    lista = list(frase)
    while i<len(lista):
        if lista[i] not in 'aãáâàeéêiíoóôuú':
            lista[i] = str.upper(lista[i])
        i = i + 1
    return str.join('',lista)
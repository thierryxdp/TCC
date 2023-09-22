def uppCons(frase):
    '''Função que recebe uma frase e retorna as suas consoantes em 
    	maiúsculas e os demais caracteres como se encontravam
        
        str -> str'''
    i=0
    lista = list(frase)
    while i<len(lista):
        if lista[i] not in 'AÃÁÂÀEÉÊIÍOÓÔUÚaãáâàeéêiíoóôuú':
            lista[i] = str.upper(lista[i])
        i = i + 1
    return str.replace(str.join('+',lista),'+','')
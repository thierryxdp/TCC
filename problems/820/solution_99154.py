def posLetra(string,letra,n):
    '''retorna a primeira vogal da palavra
    str->str'''
    i=n
    
    while i<len(string):
        if letra in string[:n]:
            posicao= string[i].find(letra,n)
            return posicao
        
    return posicao
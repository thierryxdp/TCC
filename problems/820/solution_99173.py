def posLetra(string,letra,n):
    '''retorna a primeira vogal da palavra'''
    '''str->str'''
    i=n
    conta= str.count(string,letra,n)
    encontrar= string[n].find(letra,n)
    while i<len(string):
        if conta<1:
            if letra in string:
                posicao= string[i].find(letra,n)
                return posicao
            else:
                return encontrar
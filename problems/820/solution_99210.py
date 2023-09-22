def posLetra(frase,letra,n):
    '''recebe uma string, uma letra, um número e retorna em que posição da string ocorre a letra desejada'''
    '''str,str,int->int'''
    i = 0
    posicao = []
    while i < len(frase):
        if frase[i] == letra:
            pos = str.find(frase,letra,i)
            posicao += [pos,]
        i = i + 1
    if len(posicao)<n:
        return -1
    else:
        return posicao[n-1]
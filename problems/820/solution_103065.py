def posLetra(string,letra,numero):
    '''Função que retorna a posição de uma substring em uma ocorrência desejada
    string, string, int -> int'''
    posicao=string.find(letra)
    while posicao>=0 and numero>1:
        if letra!=string:
        	return -1
        posicao=string.find(letra,posicao+1)
        n=n-1
    return posicao
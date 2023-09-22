def posLetra(string,letra,n):
    '''funcao que recebe como entrada uma string, uma letra e um numero que indica a ocorrencia desejada da letra e retorna em que posicao da string aquela ocorrencia da letra esta
    str, str, int ->int'''
    i=0
    a=str.count(string,letra)
    b=0
    if letra not in string:
        return -1
    if n>a:
        return -1
    while b != n:
    	if string[i]==letra:
            b=b+1
        i=i+1
    return b
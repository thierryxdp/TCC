def posLetra(string,letra,n):
    '''funcao que recebe como entrada uma string, uma letra e um numero que indica a ocorrencia desejada da letra e retorna em que posicao da string aquela ocorrencia da letra esta
    str, str, int ->int'''
    a=str.count(string,letra)
    if letra not in string or n>a:
        return -1
    b=0 #numero de vezes que a letra escolhida aparece antes de chegar a quantidade n
    i=0
    while b != n:
        if string[i]==letra:
            b=b+1
        i=i+1
   	return i-1
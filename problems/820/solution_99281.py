def posLetra(s,letra,n):
    '''funcao que recebe como entrada uma string s, uma letra e um numero inteiro n e retorna em que posicao da string aquela ocorrencia da letra esta
    str, str, int -> int'''
    i=0
    while i<len(s):
        i=str.find(s,letra,i+1)
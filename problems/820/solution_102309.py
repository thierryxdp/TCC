def posLetra(s,letra,n):
    '''funcao que recebe como entrada uma string s, uma letra e um numero inteiro n e retorna em que posicao da string aquela ocorrencia da letra esta
    str, str, int -> int'''
    i=0
    ocorrencia=0
    if n>str.count(s,letra) :
        return -1
    while i<len(s):
        if s[i]==letra:
            ocorrencia=ocorrencia+1
            if ocorrencia==n:
                return i
        i=i+1
def posLetra(s,letra,n):
    '''funcao que recebe como entrada uma string s, uma letra e um numero n, e retorna em qual posicao da string aquela ocorrencia da letra esta
    str, str, int -> int'''
    i=0
    ocorrencias=[]
    while i<len(s):
        if s[i]==str(letra):
            ocorrencias=ocorrencias+[s[i],]
        i=i+1
    return ocorrencias
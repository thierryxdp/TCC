def posLetra(string,letra,n):
    '''Dada uma string, uma letra e um número n, retorne a posição da string da ocorrência que a letra está; str,str,int ->int'''
    c=str.count(string,letra)
    if letra not in string or n>c:
        return -1
    i=0
    s=0
    while i<len(string):
        if string[i]==letra:
            s=s+1
        if s==n:
            return i
        i=i+1
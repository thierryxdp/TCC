def posLetra(s,l,n):
    'Dada uma string s, uma letra l e o número n de ocorrência de l, retorna o índice da n-ésima ocorrência de l'
    if str.count(s,l)>=n:
        a=str.replace(s,l,'*',n)
        b=a[::-1]
        c=str.index(b,'*')
        d=len(s)-c-1
        return d
    else:
        return -1
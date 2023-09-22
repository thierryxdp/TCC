def posLetra(s,c,n):
    '''
    retorna em que posição da string s a ocorrencia de numero n do caractere c
    str,str,int->int
    '''
    if n>s.count(c):
        return -1
    else:
        i=0
        while i<=(s.count(c)-n):
            b=s.rfind(c)
            s=s[:b]
        i=i+1
        return s.rfind(c)
posLetra('é o que contarei no outro capítulo', 'o', 4)
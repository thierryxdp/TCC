def posLetra(f,l,n):
    '''Calcula e retorna em que posição da frase(f) a letra(l) está, de acordo com o número indicado da ocorrência(n).
    str,str,int-->int'''
    i=0
    pos=0
    if str.count(f,l)<n:
        return -1
    while i<=str.index(f,l,-1):
        if f[i]==l:
            pos=pos+1
        else:
            pos
    return pos
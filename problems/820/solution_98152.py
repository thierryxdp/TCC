def posLetra(f,l,n):
    '''Calcula e retorna em que posição da frase(f) a letra(l) está, de acordo com o número indicado da ocorrência(n).
    str,str,int-->int'''
    i=0
    frase=''
    if str.count(frase,l)<n:
        i=-1
    while i<=str.index(frase,l,-1):
        if f[i]==l:
            i=i+1
        else:
            i=0
    return i
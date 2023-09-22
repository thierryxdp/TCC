def ultimapos(f,l):
    '''AGGSJSJAJ.
    str-->int'''
    i=1
    v=0
    u=0
    while str.count(f[0:i],l)<str.count(f,l):
        v=f[u]
        u=u+1
        i=i+1
    return u
def posLetra(f,l,n):
    '''Calcula e retorna em que posição da frase(f) a letra(l) está, de acordo com o número indicado da ocorrência(n).
    str,str,int-->int'''
    if str.count(f,l)<n:
        return -1
    t=ultimapos(f,l)
    frase=f[:t+1]
    i=len(frase)-1
    while str.count(frase,l)>=n:
        valor=i
        frase=frase[:t-1]
        i=i-1
    return valor
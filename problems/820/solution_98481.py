def ultimapos(f,l):
    '''Calcula e retorna a posição final da letra(l) na frase(f).
    str-->int'''
    i=1
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
    i=ultimapos(f,l)
    p=i+1
    frase=f[:p]
    i=len(frase)-1
    while str.count(frase,l)>=n and i<len(frase):
        valor=i
        p=p-1
        i=i-1
        frase=frase[:p]
    return valor
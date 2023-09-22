def posLetra(f,l,n):
    '''Calcula e retorna em que posição da frase(f) a letra(l) está, de acordo com o número indicado da ocorrência(n).
    str,str,int-->int'''
    if str.count(f,l)<n:
        return -1
    n=str.find(f,l,-1)+1
    fr=f[:n]
    valor=len(fr)+1
    i=-1
    while str.count(fr,l)>n:
        if fr[i]==l:
            valor=valor-1
        n=n-1
        f=f[0:n]
    return valor
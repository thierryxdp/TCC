def posLetra(f,l,n):
    '''Calcula e retorna em que posição da frase(f) a letra(l) está, de acordo com o número indicado da ocorrência(n).
    str,str,int-->int'''
    if str.count(f,l)<n:
        return -1
    b=str.find(f,l,-1)+1
    fr=f[:b]
    valor=len(fr)
    i=-1
    q=str.count(fr,l)
    while q>n:
        if fr[i]==l:
            valor=valor-1
        b=b-1
        f=f[0:b]
        q=str.count(fr,l)
    return valor
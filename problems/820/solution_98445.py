def posLetra(f,l,n):
    '''Calcula e retorna em que posição da frase(f) a letra(l) está, de acordo com o número indicado da ocorrência(n).
    str,str,int-->int'''
    if str.count(f,l)<n:
        return -1
    t=str.find(f,l)
    frase=f[:t+1]
    i=len(frase)-1
    while str.count(frase,l)>=n:
        if frase[i]==l or frase[i]!=l:
            valor=i
        frase=frase[:t-1]
        i=i-1
    return valor
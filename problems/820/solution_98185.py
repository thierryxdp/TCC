def posLetra(f,l,n):
    '''Calcula e retorna em que posição da frase(f) a letra(l) está, de acordo com o número indicado da ocorrência(n).
    str,str,int-->int'''
    if str.count(f,l)<n:
        return -1
    n=str.find(f,l,-1)
    frase=f[:n]
    valor=0
    i=-1
    while str.count(frase,l)>n:
        if frase[i]==l:
            valor=len(frase)-1
        n=n-1
        frase=frase[:n]
    return valor
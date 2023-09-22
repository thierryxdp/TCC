def posLetra(f,l,n):
    '''Calcula e retorna em que posição da frase(f) a letra(l) está, de acordo com o número indicado da ocorrência(n).
    str,str,int-->int'''
    i=0
    pos=0
    if str.count(f,l)<n:
        return -1
    else:
        return str.index(f,l,n)
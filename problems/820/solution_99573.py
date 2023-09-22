def posLetra(s,l,o):
    '''Retorna o indice da ocorrencia o de uma letra l em uma dada
    frase f; str,str,int -> int'''
    sn = ""
    i = 0
    while i<str.count(s,l):
        if o<str.count(s,l):
            return -1
        sn += s[i]
        i+=1
    return len(sn)
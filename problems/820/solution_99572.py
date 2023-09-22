def posLetra(s,l,o):
    '''Retorna o indice da ocorrencia o de uma letra l em uma dada
    frase f; str,str,int -> int'''
    sn = ""
    i = 0
    while i<str.count(f,l):
        if o<str.count(f,l):
            return -1
        sn += f[i]
        i+=1
    return len(sn)
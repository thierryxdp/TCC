def posLetra(frase,letra,ocorrencia):
    '''Retorna em que posição da frase a ocorrência dada da letra está. Caso hajam menos ocorrências na frase que o indicado, será retornado -1;
    str, str, int -> int'''
    i=0
    n=0
    if str.count(frase,letra)<ocorrencia
    return -1
    while i<len(frase) and n<ocorrencia:
        if frase[i]==letra:
            n=n+1
        i=i+1
    return i
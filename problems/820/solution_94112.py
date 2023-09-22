def posLetra(frase,letra,ocorrencia):
    """essa função recebe uma string, letra e um número e retorna a posição que se encontra determinada letra;
    str,str,str-> int ou str"""
    i=0
    n=0
    while i<len(frase) and n<ocorrencia:
        if frase[i] == letra:
            n=n+1
        i=i+1
    if n<ocorrencia:
        return -1
    else:
        return i-1
def posLetra(frase,letra,ocorrencia):
    """Para retornar em que posição da string a ocorrencia está, digite;
    str,str,str-> int ou str"""
    i=0
    n=0
    while i<len(frase) and n<ocorrencia:
        if frase[i] == letra:
            n=n+1
    elif n<ocorrencia:
        return -1
    else:
        return i-1
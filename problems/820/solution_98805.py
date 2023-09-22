def posLetra(frase,letra,ocorrencia):
    """essa função recebe uma string, uma letra contida nessa
    nessa string e um número que representa a ocorrência 
    desejada dessa letra e retorna em qual posição aquela letra
    se encontra;
    str,str,int--->int"""
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
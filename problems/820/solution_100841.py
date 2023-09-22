def posLetra(string,letra,ocorrencia):
    """dado uma string, uma letra e a ocorrência desejada da letra,
    a função retorna em que posição da string aquela ocorrência da letra está;
    str,str,int->int"""
    contador=0
    indice=0
    while contador<ocorrencia:
        while indice<=(len(string)-1):
            if letra==string[indice]:
                contador=contador+1
            indice=indice+1
    return indice
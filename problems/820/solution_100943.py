def posLetra(string,letra,ocorrencia):
    """dado uma string, uma letra e a ocorrência desejada da letra,
    a função retorna em que posição da string aquela ocorrência da letra está;
    str,str,int->int"""
    indicesocorrencias=[]
    indice=0
    while indice<=(len(string)-1):
        if string[indice]==letra:
            list.append(indicesocorrencias,indice)
        indice=indice+1
    if ocorrencia>len(string):
        return -1
    else:
        return indicesocorrencias[ocorrencia-1]
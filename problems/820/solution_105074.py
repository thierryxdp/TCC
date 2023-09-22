def posLetra (string,letra,n):
    """retorna em que posição da string aquela ocorrência da letra está, caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1"""
    proximo=0
    ocorrencia=0
    while ocorrencia<n:
        if proximo<len(string) and string[proximo]=='letra' or string[proximo]==str.upper('letra'):
            ocorrencia=ocorrencia+1
        proximo=proximo+1
    return ocorrencia
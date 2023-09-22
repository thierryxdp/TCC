def posLetra(S,l,n):
    """Funcao que recebe como entrada uma string S, uma
    letra l e um numero n que indica a ocorrencia desejada
    da letra (1 para primeira ocorrencia, 2 para segunda,
    etc). A funcao retorna em que posicao da string aquela 
    ocorrencia da letra esta. Caso exista menos ocorrencias 
    da letra do que a ocorrencia pedida, a funcao retorna -1;
    str,str,int->int"""
    
    ocorrencias=str.count(S,l)
    
    if ocorrencias>=n:
        return str.index(S,l,n)
    if ocorrencias<n:
        return -1
def posLetra(s,l, n):
    ''' Funcao que dada uma string, uma letra e um numero,que
    indica a ocorrencia desejada da letra, retorna em que 
    posicao da string aquela ocorrencia da letra esta, retornando
    -1 caso existam menos ocorrencias reais do que a pedida
    Parametros:
    Str,str,int
    Saida: int
    '''
    h=0
    i=-1
    
    if str.count(s,l)< n:
        return -1
    while h<= n:
        if s[i] == l:
            h= h+1
        i = i+1
    
    return i
def posLetra(string, letra, ocorrencia):
    '''Recebe como entrada uma string, uma letra e um numero
    que indica a ocorrencia desejada da letra. Retorna em que
    posicao da string aquela ocorrencia da letra esta. Caso 
    exista menos ocorrencias do que a foi pedida, a funcao 
    retorna -1
    str -> int'''
    
    s=string
    l=letra
    o=ocorrencia
    i=1
    ind=0
    
    while i<=o:
        ind=str.find(s,l,ind)+1
        i=i+1
    
    return ind
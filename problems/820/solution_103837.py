def posLetra(palavra,l,n):
    '''
    Funçao que dado uma string, uma letra e um numero que indica
    a ocorrencia desejada da letra e retorna a posiçao da 
    string em que a ocorrencia da letra esta 
    '''
    i=0
    while i<len(palavra):
        c=str.count(palavra,l,)
        m=str.find(palavra,l,0,palavra[c])
        i=i+1
    return m
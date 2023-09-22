def posLetra(s,l,n):
    '''Recebe uma string, uma letra e um numero(que indica a ocorrencia
    desejada da letra), e retorna a posiçao da ocorrencia da letra na string
    caso exista menos ocorrencias da letra do que a pedida retornara -1;
    str,str,int - > int'''
    cnt=0
    corte=0
    if n == 1:
        return str.find(s,l)
    if l not in s:
        return -1
    if l in s:
        while cnt<n:
            corte = str.find(s,l,corte)+1
            cnt=cnt+1
    return corte
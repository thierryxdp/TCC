def posLetra(string,l,n):
    '''retorna a posição da string onde a occorência n da letra acontece
    str,str,int->int'''
    q=str.count(string,l)
    i=0
    ocorrencias_anteriores=0
    if l not in string or n>q:
        return -1
    while ocorrencias_anteriores!=n:
        if string[i]=l:
        	ocorrencias_anteriores=ocorrencias_anteriores+1
        elif posicao!=l:
        	i=i+1
    return i-1
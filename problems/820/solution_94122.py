def posletra(frase,letra,num):
    '''função que retorna a posição da string que o numero está'''
    '''str,str,str-->int ou str'''
    i=0
    a=0
    while i<len(frase) and a<num:
        if frase[i]==letra:
            a=a+1
        i=i+1
    if a<num:
        return -1
    else:
        return i-1
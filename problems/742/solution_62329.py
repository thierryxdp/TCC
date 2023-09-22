def substitui(s,x,i):
    '''
    Retorna a string s e subsitui a posicao i por x
        Parametros:
            s,x,i: str,str,int
        saida: str
    '''
    if i==0:
        return x + s[1:]
    elif i==len(s):
        return s[0:(len(s)-1)] + x
    else:
        return s[0:(i)] + x + s[(i+1):]
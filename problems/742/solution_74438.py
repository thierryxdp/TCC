def substitui(s,x,i):
    '''assinatura: str,int,int > str
    casos de teste:'''
    return str(s[i+1:]) + str(x) + str(s[0:i])
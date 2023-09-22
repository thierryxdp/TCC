def substitui(s,x,i):
    '''assinatura: str,int,int > str
    casos de teste: substitui('xi','o',0) ==oi
    substitui('uemmerson','w',0) ==wemmerson
    substitui('nata','d',2) ==nada'''
    return str(s[0:i]) + str(x) + str(s[i+1:])
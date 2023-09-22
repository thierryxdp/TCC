def substitui(s,x,i):
    '''assinatura: str,int,int > str
    casos de teste: substitui('xi','o',0) ==oi
    substitui('xanys','j',0) ==janys
    substitui('cedto','r',2) ==certo'''
    return str(s[0:i]) + str(x) + str(s[i+1:])
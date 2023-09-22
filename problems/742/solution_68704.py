def substitui(s,x,i):
    '''
    retorna a string s com indice i substituito por x
    str,str,int->str
    '''
    return s[0:i]+str(x)+s[(i+1):-2]
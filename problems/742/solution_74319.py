def substitui(s,x,i):
    '''escreva uma função definida por substitui(s,x,i) e retorne uma string igual a s'''
    s[i]=x
    return s[0:i]+x+s[i+1:]
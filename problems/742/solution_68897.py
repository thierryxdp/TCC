def substitui(s,x,i):
    '''substitui a posição de uma string'''
    a1=i+1
    resultado = s[0:i]+x+s[a1:len(s)]
    return resultado
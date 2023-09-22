def substitui(s,x,i):
    '''Função que substitui um elemento de uma string s da posição i por
    um caractere x. str,str,int->str'''
    return s[0:i]+x+s[i+1:]
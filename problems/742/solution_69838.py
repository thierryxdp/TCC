def substitui(s,x,i):
    '''Função que substitui o item de posição i
    na string s pelo caractere x
    str,str,int->str'''
    s1 = s.replace(s[i],x)
    return s1
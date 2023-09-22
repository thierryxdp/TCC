def substitui(s,x,i):
    """retorna uma string igual a s que substitui o elemento da posição i pelo caractere x str,str,int-> str"""
    if i==0:
        return x+s[1:]
    elif i==len(s):
        return s[0:len(s)]+x
    else:
        return s[0:i]+x+s[1:i]
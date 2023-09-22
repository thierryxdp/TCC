def substitui(s,x,i):
    """substitui uma posição na string por um caractere i
    str,str,int->str"""
    
    return str(s[0:i])+str(x)+str(s[i+1:])
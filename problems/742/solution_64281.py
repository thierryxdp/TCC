def substitui(s,x,i):
    """retorna uma string s com o caractere x substituido por um numero i"""
    
    if i==0:
        return x + s[1:]
    else:
        return s[0:i] + x + s[i+1:]
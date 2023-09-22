def substitui(s,x,i):
    """retorna uma string igual a string s, porem com alteraçao no caracter do indice i por um caracter x, i deve ser um numero inteiro
    str,str,int--->str"""
    return s[0:i]+str(x)+s[i+1:]
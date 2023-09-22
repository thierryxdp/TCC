def substitui(s,x,i):
    """retorna uma string igual a string s, porem com alteraçao no indice i por um caracter x
    str,str,int--->str"""
    return s[0:i]+str(x)+s[i+1:]
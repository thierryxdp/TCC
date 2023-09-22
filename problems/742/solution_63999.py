def substitui(s,x,i):
    ''' retorna uma string igual a s,apenas com o elemento
    de posiçao i substituido por x;
    str,str,int -> str'''
    return s[0:i]+x+s[i+1:]
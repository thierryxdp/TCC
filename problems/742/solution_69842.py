def substitui(s,x,i):
    """ retorna uma string igual a s mas o elemento na posiçao i deve ser substituido pelo elemento da posição x
    str , int , int -> str"""
    s=str(s)
    return s[0:i]+str(x)+s[i+1:]
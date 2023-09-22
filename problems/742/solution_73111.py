# string int, int -> string
def substitui(s,x,i):
    """str,str,int ->str. Função que substitui um termo dentro da string,dado o elemento da posição referente a variável i."""
    return s[0:i]+str(x)+s[i+1:]
def substitui(s,x,i):
    """função que substitui o elemento de posição 'i' da str 's' pelo caractere 'x'. str,int,int->str"""
    return str(s).replace(str(s)[i:i],x)
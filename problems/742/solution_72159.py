def substitui(s,x,i):
    """função que substitui o elemento i da str s pelo caractere x. str,int,int->str"""
    mensagem=s[0:i]+str(x)+s[i+1: ]
    return mensagem
def substitui(s,x,i):
    """função que substitui o elemento i da str s pelo caractere x. str,int,int->str"""
    s[i]=x
    return s.replace(s[i],str(x))
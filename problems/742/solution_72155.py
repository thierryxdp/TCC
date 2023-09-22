def substitui(s,x,i):
    """função que substitui o elemento i da str s pelo caractere x. str,int,int->str"""
    return s.bytearray((s[i],str(x))
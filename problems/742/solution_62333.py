def substitui(s,x,i):
    """funcao que substitui o elemento da posicao i por x
    entrada: s= str
    		 x= str
             i= int
     saida: str"""
    return s[:i] + x + s[i+1:]
def substitui(s,x,i):
    """retorna a string 's' substituindo o caractere na localização 'i' pelo caractere 'x'.
   str,int,int ->str"""
    return s[0:i] + x + s[i+1:]
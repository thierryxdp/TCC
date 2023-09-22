def substitui(s,x,i):    
    """A função vai substituir o caractere "x" na posição "i" da string "s" e vai retornar 
uma string com a substituição. string,string,int-->string"""
    return s[0:i]+x+s[i+1::1]
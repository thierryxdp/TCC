def substitui(s,x,i):
    """recebe uma string s,um caractere x e um numero inteiro i entre 0
    e o comprimento da string, e retorna um string igual a s,somente
    trocando o elemento da posicao i pelo caractere x. int,int->string"""
    
   return s[0:i]+x+s[i+1:]
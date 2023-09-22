# string, int, int -> string
def substitui(s,x,i):
    """recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string, e retorna uma string igual a s mas com o elemento da posicao i substituido pelo caractere x
    string, int, int -> string"""
    y=i+1
    h=len(s)
    p=s[0:i]+x+s[y:h]
    return p
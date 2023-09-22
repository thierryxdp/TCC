# string, int, int -> string
def substitui(s,x,i):
    """recebe uma string s, um caractere x e um inteiro i e retorna uma string igual a s exceto que o elemento de index i é substituido por x """
    return s[0:i]+x+s[i+1:]
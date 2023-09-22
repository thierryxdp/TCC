def substitui(s,x,i):
    """ com um string s, caractere x e um numero inteiro i entre
    0 e o comprimento da string; retorna a string s e substitui i com x;
    str, str, int -> str"""
    return s [0 : i] + str(x) + s [i + 1 : len(s) - (s+i)]
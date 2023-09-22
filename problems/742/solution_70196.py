def substitui(s,x,i):
    'dados uma str s, um caractere x e um int i situado entre 0 e comprimento da str, retorna a str s tendo seu caracter da posicao i substituido por x str, int, int -> str'
    (s.split)[i]=x
    return s.join(s.split)
def substitui(s,x,i):
    'Retorna uma string igual a s, mas com o caractere x na posicao i, com 0<=i<=int(len(s)). Str, str, int -> str'
    return s[0:i]+x+s[(i+1):]
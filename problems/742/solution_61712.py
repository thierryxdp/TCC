def substitui(s, x, i):
    ''''''''' funcao que recebe uma string s, um caractere x e um numero inteiro i;
    str , str , int -> str '''''''''
    return s[0:1] + x + s[i+1:len(s)];
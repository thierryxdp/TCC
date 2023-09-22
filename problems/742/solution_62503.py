def substitui(s,x,i):
    """Função que recebe uma string s, caractere x e um numero inteiro i entre 0 e o sendo comprimento da string e retorna uma string s
    str, str, int -> str"""
    return s[0:i] + x + s[i+1:len(s)]
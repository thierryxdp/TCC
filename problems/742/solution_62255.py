def substitui(s,x,i):
    """Funcao que recebe uma string s, um caractere x e um numero inteiro
    i entre 0 e o comprimento da string, e retorna uma string igual a s,
    exceto pelo fato de que o elemento da posicao i e substituido pelo
    caractere x;
    str,str,int->str"""
    return s[0:i]+x+s[i+1:]
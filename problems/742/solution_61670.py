def substitui(s,x,i):
    ''' função que recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string, e retorna a string com a letra x na posição do elemento i;
    str, str, int -> str'''
    sbs=len(s)//2
    return s[0:i] + x + s[i+1:len(s)]
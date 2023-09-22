def substitui(s,x,i):
    """Função que recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string, e retorna uma string igual a s,porém com o caractere x no lugar do lemento de posição i;str,int,int->str"""
    if i<=(len(s)-1):
        return s[0:i]+x+s[i+1:]
    else:
        n=i-(len(s)-1)
        return s[0:1-n]+x
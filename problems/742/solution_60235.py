def substitui(s,x,i):
    """Funcao que recebe uma string s, um caractere x e 
        um numero inteiro entre 0 e o comprimento da string e retorna 
        uma string igual a s substituindo i por x """
    l=list(s)
    l[i]=x
    return"".join(l)
def substitui(s,x,i):
    """Funcao que recebe uma string(s), um caractere(x) e um
    numero inteiro(i) e retorna uma string igual a s, mas
    subistitui i por x"""
    s[1]=x
    return s[0:i]+x+s[i+1;]
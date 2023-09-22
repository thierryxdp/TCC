def substitui(s,x,i):
    """Funcao que recebe uma string(s), um caractere(x) e um
    numero inteiro(i) e retorna uma string igual a s, mas
    subistitui i por x"""
    1=list(s)
    1[i]=x
    return "".join(1)
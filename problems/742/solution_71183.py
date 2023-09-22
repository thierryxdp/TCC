def substitui(s,x,i):
    """Função que retorne uma string igual a s, mas que tenha o elemento da posição i trocado pelo x;string, int, int -> string"""
ss = (s,x,i)
tupla = tuple(ss)
tupla[2]=x
ss = tuple(tupla)
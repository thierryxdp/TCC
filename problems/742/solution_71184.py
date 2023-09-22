def substitui(s,x,i):
    """Função que retorne uma string igual a s, mas que tenha o elemento da posição i trocado pelo x;string, int, int -> string"""
substituicao = (s,x,i)
tupla = tuple(ss)
tupla[2]=x
substituicao = tuple(tupla)
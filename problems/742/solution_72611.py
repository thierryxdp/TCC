def substitui(s,x,i):
    """ retorna uma str igual a s, exceto que o
    elemento na posicao i sera substituido pelo
    caractere x.
    str, str, int -> str"""
    inicio_de_s = s[:i]
    fim_de_s = s [1 + i:]
    return inicio_de_s + x + fim_de_s
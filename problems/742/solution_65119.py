def substitui(s,x,i):
    """ retorna o a mesma string "s", mas com x no lugar de um número dito pela variavel "s". string, int, int -> string"""
    return s[0:i-1] + x + s[i:]
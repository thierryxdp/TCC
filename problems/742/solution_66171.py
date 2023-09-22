def substitui(s,x,i):
    """ Dado como parâmetros de entrada uma string s, um carctere x
    e um número inteiro i entre 0 e o comprimento da string, será re-
    tornado uma string igual a s, exceto que o elemento da posição i
    será substituído pelo caractere x.
    string, int, int -> string"""
    nova_string = s[:i] + x + s[i:]
    return nova_string
def substitui(s,x,i):
    '''função retorna uma string "s" com seu caractere de número "i" substituido por um caractere "x"
    string, int, int -> string'''
    return s[:i] + x + s[(i+1):]
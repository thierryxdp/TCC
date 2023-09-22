def substitui(strings,x,i): 
    """retorna uma string s subititundo o i tem da posição i por x
    string, int, int -> string"""
    return strings [0:i] + x + strings[i + 1:]
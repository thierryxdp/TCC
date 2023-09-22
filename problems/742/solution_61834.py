def substitui(strings,x,i): 
    """retorna uma string s subititundo o i tem da posição i por x
    string, int, int -> string"""
    strings[i] = x
    return strings [0:i] + x + str1[i + 1:]
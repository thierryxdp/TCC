def substitui(s,x,i):
    """Retorna uma string igual a s, exceto que o elemento da posição i, deve ser substituído
    pelo caractere x
    str, str, int -> str"""
    return str(s)[0:i] + str(x) + str(s)[(i+1):len(str(s))]
def substitui(str1,x,i):
    """essa funçao retorna uma string s, a qual um de seus elementos, o da posiçao i, sera substituido pelo caractere x"""
    """entrada: str, int, int"""
    """saida: str"""
    str(str1[i]) = x
    return str1[0:i] + x + str1[i+1:]
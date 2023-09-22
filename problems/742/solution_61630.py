#substituicao
def substitui(s, x, i):
    """funcao que retorna uma string igual a s e substitui o inteiro i pelo caractere x,
       str, int, int --> str"""
    z=i+1	
    return s[:i]+x+s[z:]
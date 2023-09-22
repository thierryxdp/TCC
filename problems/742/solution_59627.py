# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna a string informada com o caracter 'x' substituindo na posição 'i'"""
    """ entradas: str, str, int
    saida: str"""
    return s[0:1] + x + s[i+1:]
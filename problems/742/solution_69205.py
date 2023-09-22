# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma nova string com um carctere substituído de acordo com a posição dado pela entrada i
    str, int, int -> str"""
    return s[:i] + x + s[i+1:]
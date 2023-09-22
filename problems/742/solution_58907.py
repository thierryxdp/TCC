# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Essa função substitui um caractere de uma string com outra
    s: str -> str Texto inicial
    x: str -> str Alteração
    i int -> int Posição onde x substitui s"""
    return s[:i] + x + s[i+1:]
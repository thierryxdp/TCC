# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que substitui um caractere por um outro carectere,
    str + str + int --> str"""
    return s[:i] + x + s[i + 1:]
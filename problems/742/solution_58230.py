# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Definição"""
    antes = s[:i]
    depois = s[i+1:]
    return antes + x + depois
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna a string s com o caractere numero i trocado pelo x
    str, int, int --> string"""
    buffer = s[:i] + str(x) + s[i + 1:]
    return buffer
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna a string s, mas com o caractere da posição i trocado com o caratere x.
    string, int, int -> string"""
    return s[:i] + x + s[i + 1:]
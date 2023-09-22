# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string igual a s, entretanto com o caractere
    de índice i, subtituido pelo caractere x;
    string, string, int -> string"""
    return s[:i] + x + s[i+1:]
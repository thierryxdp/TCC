# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que, recebida uma string s que contém o
    caractere x, retorna s porém com o caractere i no lugar
    de x;
    string, int, int -> string"""
    Stringi = s - s[x] + s[i]
    return stringi
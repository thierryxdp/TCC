# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorne a string com o caracter x no indice i da string s;
    string, string, int -> string"""
    return s[:i]+x+s[i+1:]
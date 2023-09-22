# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que troca o elemento da posição i da string s pelo caractere x
    string, int, int -> string"""
    return s[:i] + str(x) + s[i+1:]
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """recebe uma string(s) e substitui o caractere de posição(i) pelo caractere(x). string, int, int -> string"""
    string=str(s)
    return string[i:]+x+string[:i]
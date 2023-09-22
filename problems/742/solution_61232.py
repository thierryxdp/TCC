# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """substitui um valor x  de uma string s por uma letra na posição i; str, str, int -> str"""
    return s[0:i]+str(x)+s[i+1:]
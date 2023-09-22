# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """
    fruncao retorna com um termo de numero i da palavra substituido pelo x
    """
    return str(s[0:i]+x+s[i+1:])
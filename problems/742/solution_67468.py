# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Substitui o valo i por x na str s"""
    h=s[i+1:]
    return (s[:i]+'x')+h
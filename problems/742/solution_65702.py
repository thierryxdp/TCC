# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """substitui na string "s"colocando x na posição de i. """
    if i>=0 and i<=len(s):
        return s[0:(i)]+x+s[(i+1):]
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ funcao que retorna o elemento 
        da posicao i substituido pelo termo x."""
    return s[:i]+x+s[i+1:]
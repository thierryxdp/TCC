# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna string s mas o elemento da posicao i vai ser substituido pelo x"""
    return s[:i]+str(x)+s[i+1:]
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que insere x numa posicao qualquer da string"""
    """string, int ,int -> string"""
    i >= 0 and i <= len(s)
    return s[:i]+x+s[i+1:]
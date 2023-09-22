# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Funcao que retorna a string s, exceto o elemento da posicao i, que é substituido pela string x."""
    subs= s[i:1]
    return s.replace(subs, x)
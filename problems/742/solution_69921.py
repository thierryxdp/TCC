# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'funçao que retorn uma str com a variavel i trocada pelo x'
    s[1]= x
    return s[0:1] + x + s[1 + 1:]
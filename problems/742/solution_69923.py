# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(str1,x,i):
    'funçao que retorn uma str com a variavel i trocada pelo x'
    str1[i] = x
    return str1[0:i] + x + str1[i + 1:]
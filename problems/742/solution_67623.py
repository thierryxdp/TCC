# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    palavra1 = s[:i+1]
    palavra2 = s[i:]
    palavra = palavra1 + palavra2
    return palavra
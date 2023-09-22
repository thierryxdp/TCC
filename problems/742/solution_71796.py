# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    new_s=s
    return new_s[0:i] + x + new_s[i + 1:]
    return new_s
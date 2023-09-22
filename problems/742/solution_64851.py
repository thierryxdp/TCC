# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    meio = len(s)//i-1
    return str(s)[0:meio] + x + str(s)[meio:]
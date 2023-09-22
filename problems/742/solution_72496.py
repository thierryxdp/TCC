# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    b = bytearray(s)
    b[i] = 'x'
    s = str(b)
    print s
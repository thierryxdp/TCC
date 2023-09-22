# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    saida = bytearray(s)
    saida[i] = x
    s = str(saida)
    return s
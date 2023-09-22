# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    new_s = bytearray(s)
    new_s[i]=x
    s=str(new_s)
    return s
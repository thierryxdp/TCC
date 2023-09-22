# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    tam=len(s)
    if tam>i:
        letra=str.partition(s,i)
        return letra
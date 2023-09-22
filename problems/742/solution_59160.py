# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    k = len(s)
    j = round((k/2)-0.5)
    l = round((k/2)+0.5)
    m = s[:j]
    n = s[l-1:]
    return m + s + n
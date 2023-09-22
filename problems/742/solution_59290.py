# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    i = i[-1] + i[1:-1] + i[0] if len(s) > 1 else i
    substitui = s.replace(s[i],x,)
    return substitui
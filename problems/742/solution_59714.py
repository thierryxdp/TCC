# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    i = len(s)-1
    return s.replace((str(s)[int(i)]),x)
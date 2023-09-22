# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'retorna uma string igual a s'
    i>0 and i<len(s)
    s[i]=x
    p=s[:i]+x+s[i:]
    return p
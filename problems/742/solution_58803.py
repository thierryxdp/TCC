# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i>len(s)-1:
        print('codigo invalido')
    elif i:
        return s[0:i]+x+s[1+i:]
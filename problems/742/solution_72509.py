# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i >= 1:
        a = s[0:i]
        b = s[i+1:]
        return str(a) + str(x) + str(b)
    
    elif i == 0:
        a = s[i+1:]
        return str(x) + str(a)
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i<0:
    return x+s
    elif i>len(s):
        return s+x
    else: 
    return s[:i] + x+ s[i+1:]
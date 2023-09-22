# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if 0<=i<=(len(s)-1):
        return s[:i] + x s[i+1:]
    else:
        return 'i nao pode ser maior do que os caracteres da palavra'
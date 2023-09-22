# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i >= len(s) or  0 <=i:
        return s[:i] +  str[x] + s[i+1:]
    else:
        return 'nao e possivel fazer a substituicao'
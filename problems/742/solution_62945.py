# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    " Pega primeira parte da string antes de i, coloca o caractere x e depois adiciona o restante da str"
    y = s[:i] + x + s[i+1:]
    return y
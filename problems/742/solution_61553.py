# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "string,string,int--->string"
    "pega um string (s) e substitui o caractere (x) na posição (i)"
    return s[:i] + str(x) + s[i+1:]
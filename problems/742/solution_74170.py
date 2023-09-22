# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i >= 0 and i <= len(s):
        letra = s[i]
        s = str.replace(s,letra,x,1,1)
        return s
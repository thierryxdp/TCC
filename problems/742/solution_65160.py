# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    #substituindo x pelo termo s[i] de s[0:]:
    s[i] = x
    #retrnando s:
    return s[0:i] + s[i] + s[(i+1):]
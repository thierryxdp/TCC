# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    anteriorS = s[0:i-1]
    posteriorS = s[i:]
    
    return anteriorS + x + posteriorS
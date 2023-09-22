# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    anteriorS = s[0:x-1]
    posterior = s[x:]
    
    return anteriorS + i + posteriorS
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    substitui = s.replace(s[i:300],x + s[0:300])
    return substitui
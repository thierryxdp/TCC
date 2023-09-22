# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    substitui = s.replace(s[i:10000],x + s[i+1:3000000] )
    return substitui
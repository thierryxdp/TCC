# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    parte1= s[0:i]
    parte2= s[i+1:]
    return parte1+str(x)+parte2
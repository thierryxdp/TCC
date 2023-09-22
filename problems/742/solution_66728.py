# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Substitui um caractere 'x' na posição 'i' da string 's'; string, string or int, int -> string"
    x = str(x)
    troca = s[0:i]+x+s[i+1:] 
    return troca
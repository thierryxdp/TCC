# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    nova = s[:i] + x + s[i+1:]
    
    return nova

substitui("patty","a",3)
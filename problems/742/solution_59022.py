# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dado uma string s, um caractere x, e um número i, a função
    substitui a letra na posição i da string pelo caractere x 
    informado."""
    
    texto = s[0:i] + x + s[i+1:]
    return texto
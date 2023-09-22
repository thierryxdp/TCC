# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string, e retorna uma string
    igual a s, com o elemento da posicao i sendo substitudo pelo caractere x"""
    
    return s[0:i] + str(x) + s[i+1:len(s)]
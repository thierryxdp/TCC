# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string s, um caractere x e um
n umero inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s, exceto que o elemento da posição i é substituido pelo caractere de x"""
    j=i+1
    z=s[0:i]
    y=s[i:]
    return z+'x'+y
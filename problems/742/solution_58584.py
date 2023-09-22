# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """
    Função que dada uma string s, um caractere x e um número inteiro i entre o e o comprimento da string,
    retorna a string s com o elemento da posição i substituído pelo caractere x
    """
    return (s[0:i]+x+s[i+1:])
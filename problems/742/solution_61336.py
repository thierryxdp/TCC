# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Funçao que retorna uma string igual a s, e o elemento da posicao i vire o caractere x.
    string, int, int - > string"""
    return s[0:i]+str(x)+s[i+1:]
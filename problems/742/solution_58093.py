# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dados uma string s, um caractere x e um numero inteiro x, que esteja
    entre 0 e o comprimento da string, a funcao retorna a string s com o
    caractere x na posicao i
    """
    substituicao = s[:i] + str(x) + s[i + 1:]
    return substituicao
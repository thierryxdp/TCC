# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """
    Função que substitui um caractere de uma string por outro fornecido na posição desejada.
    """
    final=len(s)
    return s[0:i]+x+s[i+1:final]
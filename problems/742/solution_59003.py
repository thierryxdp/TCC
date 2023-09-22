# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Funcao que substitui o elemento da string s posicao i pelo caractere x """
    inicio = s[0:i]
    final = s[(i+1):]
    
    return inicio+x+final
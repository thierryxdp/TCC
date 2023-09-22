# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """recebida uma string s, um caractere x e um número inteiro i
    entre 0 e o tamanho da string, retorna a string s com o caractere x na posição i 
    dessa string. str, str, int -> str"""
    return s[0:i]+x+s[i+1:]
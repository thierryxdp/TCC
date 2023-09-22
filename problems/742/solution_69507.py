# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s:str,x:str,i):
    """Função que recebe uma string s e adiciona um caractere(x) no local do caractere de posição i"""
    return s[0:i]+x+s[i+1:]
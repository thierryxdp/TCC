# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma palavra com um caractere alterado,dados a palavra,o caractere 
       a ser adicionado e a posição do caractere que deve ser substituído"""
    return s[0:i]+x+s[(i+1):]
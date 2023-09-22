# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """essa funçao substitui uma posiçao na string em um caractere desejado"""
    return s[0:i]+str(x)+s[i+1:len(s):1]
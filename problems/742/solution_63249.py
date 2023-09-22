# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """substitui o caractere no indice i de uma string s por um caractere x"""
    resultado=s[0:i]+x+s[i+1:len(s)]
    return resultado
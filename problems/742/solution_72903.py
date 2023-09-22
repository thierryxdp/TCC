# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string igual a s, substituindo o elemento i por x"""
    frase=i+1
    return s[0:i]+x+s[frase:]
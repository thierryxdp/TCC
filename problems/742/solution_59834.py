# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string igual a s, substituindo um caracter localizado na posição i pelo x"""
    substitui = (s, x, i)
    return s[0:i] + x + s[i+1::]
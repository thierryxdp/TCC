# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Troca um caractere da string por uma letra qualquer, desde que informado a posição que essa letra deve estar
    str, int, int -> str"""
    return {s[0:i]}+{x}+{s[i+1:]}
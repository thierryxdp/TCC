# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Troca um caractere da string por uma letra qualquer, desde que informado a posição que essa letra deve estar
    str, str, int -> str"""
    return f"{s[0:i]}{i}{s[i+1:]}"
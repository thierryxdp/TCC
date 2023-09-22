# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que retorna a string dada substituindo a posição de inteiro dada pelo caractere dado str, str, int -> str"""
    return s[:i] + x + s[i+:]
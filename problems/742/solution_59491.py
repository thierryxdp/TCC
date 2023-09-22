# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Recebe uma string s, um caractere x e um número inteiro i e retorna 
    a mesma string substituindo o elemento da posição i pelo caractere x"""
    return s[:i] + x + s[i+1:]
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um numero inteiro i e retorna a mesma string s porém com o elemento da posição i substituído por x'''
    string = s
    0 < i < len(s)
    return s[:i] - s[i] + 'str(x)' + s[i:]
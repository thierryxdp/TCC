# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x, i):
    ''' Resulta na troca do elemento de posição i por outro elemento x dentro de uma
        string s, a função se separa do elemento de posição i e retorna com o elemento x'''
    return s[:i]+x+s[i+1:]
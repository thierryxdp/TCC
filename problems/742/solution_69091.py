# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'funcao que recebe uma string s, u caractere x e um numero
    'inteiro i e retorna ua string igual a s'
    return s[:i]+x+s[i+1:]
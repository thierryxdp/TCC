# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string s, um caractere x e um número
    inteiro i entre 0 e o comprimento da string, e retorna s, sendo
    que x substitui o elemento do caractere i;
    string, int, int -> string"""
    s = s[0:i] + x + s[i+1:-1]
    return s
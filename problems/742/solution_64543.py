# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string, e retorna uma string igual s, exceto que o elemento da posição i deve ser substituído pelo caractere x.
    string, string, int->string"""
    return str(s[0:i])+str(x)+str(s[i+1:])
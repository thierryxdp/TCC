# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string 's', um caractere 'x' e um número inteiro 'i' entre 0 e o comprimento da string, e retorna uma string igual a 's', e o elemento da posição 'i' substituido por 'x'; str, str,int -> str"""
    return s[:i]+x+s[i+1:]
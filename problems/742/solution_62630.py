# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna, dado uma string 's', um caractere 'x'
    e um número inteiro 'i' entre 0 e o comprimento da
    string, uma string igual a s com o elemento da posição
    'i' substituído por 'x'
    str,int,int -> str"""
    return s[0:i]+x+s[i+1:]
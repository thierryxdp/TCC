# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dada uma string 's', um caractere 'x' e um número inteiro 'i', cujo valor deve compreender entre 0 e o comprimento da string. A função
    retorna uma string igual a 's', contudo o elemento da posição 'i' é subistutuído pelo caractere 'x';
    str, str, int --> str"""
    a = s[0:i] + x + s[i + 1:]
    return a
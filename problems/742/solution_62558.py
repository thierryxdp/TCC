# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Função que recebe uma string 's', um caractere x e um número 
    inteiro 'i' e retorna uma igual a 's', exceto que o elemento da 
    posição 'i' deve ser subistituido pelo caractere 'x'.
    Entrada: Strig, int, int
    Saída: String"""
    s = s[0:i] + x + s[i+1:]
    return s
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(string,caractere,posicao):
    '''função que recebe uma string, um caractere e um numero e retorna uma string com o caractere substituindo o outro no lugar indicado pela posicao. str, str, int -> str'''
    return string[:posicao] + caractere + string[posicao+1:]
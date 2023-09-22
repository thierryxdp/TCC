# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorna uma nova string com base na string s e em um caractere x que
    sera substituido na posicao determinada por um numero inteiro i
    (0<i<comprimento da string);
    str, int, int -> str'''
    string = s
    return string[0,i] + caractere + string[i+1:]
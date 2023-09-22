# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui (s,x,i):
    '''retorna uma str igual a inserida o primeiro arg de entrada mas com o
    caractere x inserido na posicao i determinada pelo 3 arg, substituindo
    o caractere que ocupava essa posição em s
    str , int , int -> str'''

    return s[0:i] + x + s[i+1:len(s)]
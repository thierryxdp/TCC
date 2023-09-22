# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Recebe uma string s, um cactere x e um numero inteiro i entre 0 e o comprimento da string, e retorna uma string igual a s, onde o elemento da posicao i é substituido pelo caractere x
string, int, int -> string"""
    lista=[s]
    lista[i:]=[x]
    return lista
def substitui(s,x,i):
    """Recebe uma string s, um cactere x e um numero inteiro i entre 0 e o comprimento da string, e retorna uma string igual a s, onde o elemento da posicao i é substituido pelo caractere x
string, int, int -> string"""
    lista=[s]
    lista[1:]=x
    return lista
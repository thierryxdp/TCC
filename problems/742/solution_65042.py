def substitui(s,x,i):
    """ função que recebe string s, caractere x e número inteiro i que retorna uma string igual a s, sendo que o elemento da posição i é substituido pel]o caracter x
    string, string, int -> string"""
    return s [0:i] + x + s [(i + 1):]
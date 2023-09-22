def substitui(str1,x,i):
    """ Função que recebe 3 parametros (s,x,i) e retorna uma 
    string igual a s(string), exceto que o elemento da 
    posição i(numero inteiro) deve ser substiuído pelo
    caractere x
    : string (s); caractere (x); número inteiro (i)
    : str, int, int -> string """
    str1 = str1[0:i] + x + str1[i + 1:]
    str1 [i] = x
    return str1
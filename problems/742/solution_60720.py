def substitui(frase,caractere,n):
    #substitui a letra na posicao n da frase dada pelo caractere dado
    # string, int, int -> string
    frase = list(frase)
    frase[n] = caractere
    return frase
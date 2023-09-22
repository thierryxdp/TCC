def inverte(frase):
    '''função que dada uma frase retorna outra
    na ordem inversa de palavras, sem letras
    maiúsculas e sem a pontuação
    string -> string'''
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace(":", " ")
    lista = str.split(frase)
    lista.reverse()
    #lista = list.reverse(lista) 
    frase = str.join(" ", lista)
    #retorna sem maiúsculo
    return frase.lower()
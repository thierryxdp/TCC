def inverte(string):
    """ Funcao que retorna a frase inserida invertida
        string -> string"""
    lista = str.split(string,)
    list.reverse(lista)
    return lower(str.join(" ",lista))
def inverte(frase):
    """Funcao que dada uma frase retorna ela com a oredem inversa
    string->string"""
    frase=str.split(frase)
    list.reverse(frase)
    return str.join ('', frase)
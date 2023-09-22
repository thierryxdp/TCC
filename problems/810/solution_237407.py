def inverte(x):
    """Funcao que dada uma frase retorna ela com a oredem inversa
    string->string"""
    frase=str.split(str,separador(x))
    list.reverse(frase)
    return str.join(separador('',frase))
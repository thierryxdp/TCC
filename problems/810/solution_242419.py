def inverte(f):
    """Dada uma frase (f) ele retorna como saída outra frase
    qie tenha as mesmas palavras da frase de entrada só que 
    inversamente."""
    lista = str.split(f)
    lista = str.replace(f)
    lista.reverse()
    f = str.join(" ", lista)
    return f
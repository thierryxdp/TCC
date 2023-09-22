def inverte(f):
    """Dada uma frase (f) ele retorna como saída outra frase
    qie tenha as mesmas palavras da frase de entrada só que 
    inversamente."""
    f = f.lower()
    f = f.replace(',', ' ')
    f = f.replace(';', ' ')
    f = f.replace(':', ' ')
    f = f.replace('...', ' ')
    f = f.replace('.', ' ')
    f = f.replace('!', ' ')
    f = f.replace('?', ' ')
    f = f.replace('-', ' ')
    lista = str.split(f)
    lista.reverse()
    f = str.join(" ", lista)
    return f
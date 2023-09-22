def contar(texto):
    import regex
    return len(texto.split("[.,...,!,?]",))
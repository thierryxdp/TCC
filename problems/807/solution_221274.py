def contar(texto):
    import re
    return re.split("[.,...,!,?]",texto)
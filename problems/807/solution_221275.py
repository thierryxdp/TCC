def contar(texto):
    import re
    return len(re.split("[.,...,!,?]",texto))
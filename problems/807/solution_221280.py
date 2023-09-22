def contar(texto):
    import regex
    return len(re.split("[.,...,!,?]",texto))
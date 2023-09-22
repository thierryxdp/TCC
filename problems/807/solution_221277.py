def contar(texto):
    
    import regex
    return len(regex.split("[.,...,!,?]",texto))
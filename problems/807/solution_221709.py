def conta_frases(texto):
    """funcao que, dada uma string(texto) com diversas frases que acabam apenas com "!,?,.,...", retorna o numero de frases que ha nesse texto
    str--->int"""
    str.replace(texto,'...','!')
    str.replace(texto,'.','!')
    str.replace(texto,'?','!')
    return len(texto)
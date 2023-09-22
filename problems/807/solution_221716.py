def conta_frases(texto):
    """funcao que, dada uma string(texto) com diversas frases que acabam apenas com "!,?,.,...", retorna o numero de frases que ha nesse texto
    str--->int"""
    texto=str.replace(texto,'...','!')
    texto=str.replace(texto,'.','!')
    texto=str.replace(texto,'?','!')
    texto=str.split(texto,'!')
    return len(texto)-1
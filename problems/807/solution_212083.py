Final = len(list(str.split(texto, '.')))
    Exclamacao = len(list(str.split(texto, '!')))
    Interrogacao = len(list(str.split(texto, '!')))
    Reticencias = len(list(str.split(texto, '...')))
    return Final + Exclamacao + Interrogacao + Reticencias - 3*Reticencias
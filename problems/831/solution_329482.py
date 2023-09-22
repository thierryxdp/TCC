def lingua_p(palavra):
    """recebe uma palavra e retorna essa traduzida para
    a lingua dop(introduz apos cada vogal a letra p e
    a mesma vogal novamente)
    str -> str"""
    for letra in palavra:
        if letra in "AEIOUaeiou":
            palavra.replace(letra,(letra+"p"+letra))
    return str.lower(palavra)
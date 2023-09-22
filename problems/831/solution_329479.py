def lingua_p(palavra):
    """recebe uma palavra e retorna essa traduzida para
    a lingua dop(introduz apos cada vogal a letra p e
    a mesma vogal novamente)
    str -> str"""
    copia=palavra
    for letra in copia:
        if letra in "AEIOUaeiou":
            str.replace(palavra,letra,(letra+"p"+letra))
    return str.lower(palavra)
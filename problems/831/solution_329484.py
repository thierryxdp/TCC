def lingua_p(palavra):
    """recebe uma palavra e retorna essa traduzida para
    a lingua dop(introduz apos cada vogal a letra p e
    a mesma vogal novamente)
    str -> str"""
    for letra in palavra:
        if letra in "AEIOUaeiou":
            fim=palavra.replace(letra,(letra+"p"+letra))
            palavra=fim
    return str.lower(fim)
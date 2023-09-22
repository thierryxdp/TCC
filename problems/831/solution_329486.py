def lingua_p(palavra):
    """recebe uma palavra e retorna essa traduzida para
    a lingua dop(introduz apos cada vogal a letra p e
    a mesma vogal novamente)
    str -> str"""
    a=0
    for letra in palavra[a:]:
        if letra in "AEIOUaeiou":
            fim=palavra.replace(letra,(letra+"p"+letra))
            a=str.index(fim,letra)
    return str.lower(fim)
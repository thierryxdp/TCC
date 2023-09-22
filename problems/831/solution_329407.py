def lingua_p(palavra):
    """recebe uma palavra e traduz essa para a lingua do
    p, adicionando um p + a vogal original apos todas 
    as vogais dessa.
    str -> str"""
    copia=palavra
    for letra in copia:
        if letra in "AEIOUaeiou":
            str.replace(copia,letra,(letra+"p"+letra))
    return str.lower(copia)
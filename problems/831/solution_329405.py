def lingua_p(palavra):
    """recebe uma palavra e traduz essa para a lingua do
    p, adicionando um p + a vogal original apos todas 
    as vogais dessa.
    str -> str"""
    for letra in palavra:
        if letra in "AEIOUaeiou":
            str.replace(palavra,letra,(letra+"p"+letra))
    return str.lower(palavra)
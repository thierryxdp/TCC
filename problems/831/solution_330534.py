def lingua_p(palavra):
    """
    str -> str"""
    palavra_minuscula str.lower(palavra)
    palavra_final = ""
    for letra in palavra_minuscula:
        palavra_final+=letra
        if letra in "aeiou":
            palavra_final+="p" + letra
    return palavra_final
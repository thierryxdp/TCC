def lingua_p(palavra):
    """Retorna a palavra traduzida para a lingua do P; string -> string."""
    for i in "aeiou":
        palavra = str.replace(palavra, i, i + "p" + i)
    return palavra
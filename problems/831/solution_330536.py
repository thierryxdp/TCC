def lingua_p(palavra):
    """Retorna uma string minúscula traduzida da original dada
    como entrada (em português) para a língua do P. Ou seja,
    após cada vogal há o acréscimo da letra p + a própria vogal.
    str -> str"""
    palavra_minuscula = str.lower(palavra)
    palavra_final = ""
    for letra in palavra_minuscula:
        palavra_final+=letra
        if letra in "aeiouáéíóúâêîôûãõ":
            palavra_final+="p" + letra
    return palavra_final
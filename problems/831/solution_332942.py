def lingua_p(palavra):
    """Retorna a palavra com p antes e depois de cada vogal;
    str -> str"""
    palavra_nova = ""
    for letra in palavra:
        if letra in "aeiouAEIOU":
            palavra_nova += letra.lower() + "p"
        else:
            palavra_nova += letra.lower()
    return palavra_nova
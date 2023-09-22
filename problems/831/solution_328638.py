def lingua_p(palavra: str) -> str:
    """comentário"""
    palavra = palavra.split().lower
    for i in palavra:
        if i == "aeiou":
            indice = palavra.index(i) + 1
            palavra.insert(indice,'p')
    return palavra
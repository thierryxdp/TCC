def lingua_p(palavra: str) -> str:
    """comentário"""
    palavra = list(palavra)
    for i in palavra:
        if i == "aAeEiIoOuU":
            indice = palavra.index(i) + 1
            palavra.insert(indice,'p')
            "".join(palavra)
    return palavra
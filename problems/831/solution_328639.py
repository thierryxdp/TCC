def lingua_p(palavra: str) -> str:
    """comentário"""
    palavra = palavra.split()
    for i in palavra:
        if i == "aAeEiIoOuU":
            indice = palavra.index(i) + 1
            palavra.insert(indice,'p')
    return palavra
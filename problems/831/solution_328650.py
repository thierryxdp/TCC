def lingua_p(palavra: str) -> str:
    """comentário"""
    palavra = list(palavra)
    for i in palavra:
        if i in "aAeEiIoOuU":
            indice = palavra.index(i) 
            palavra[indice] = i + 'p'
            "".join(palavra)
    return palavra
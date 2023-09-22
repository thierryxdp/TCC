def lingua_p(palavra: str) -> str:
    """comentário"""
    
    for i in palavra:
        if i in "aAeEiIoOuU":
            palavra = list(palavra)
            indice = palavra.index(i) 
            palavra[indice] = i + 'p'
            "".join(palavra)
    return palavra
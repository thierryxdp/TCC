def lingua_p(palavra: str) -> str:
    """comentário"""
    i = 0
    palavra = list(palavra.lower())
    for i in palavra:
        if i in "aãâáàeêiíoóôõuú":
            letra_p ='p'+ i
            palavra.insert(indice, letra_p)
    
    palavra = "".join(palavra)
    i += 0
    return palavra
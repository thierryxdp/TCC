def lingua_p(palavra: str) -> str:
    """comentário"""
    indice = 0
    palavra = palavra.lower()
    for i in palavra:
        if i in "aãâáàeêiíoóôõuú":
            palavra = list(palavra)
            letra_p ='p'+ i
            palavra.insert(indice, letra_p)
    indice += 1
    palavra = "".join(palavra)
    return palavra
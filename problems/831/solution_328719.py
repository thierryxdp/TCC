def lingua_p(palavra: str) -> str:
    """comentário"""
    i = 0
    palavra = list(palavra.lower())
    for letra in palavra:
        if letra in "aãâáàeêéiíoóôõuú":
            letra_p ='p'+ letra
            palavra[i] = letra +'p'+ letra
    	i += 1
    palavra = "".join(palavra)
    return palavra
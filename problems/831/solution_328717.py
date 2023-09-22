def lingua_p(palavra: str) -> str:
    """comentário"""
    indice = 0
    palavra = list(palavra.lower())
    for letra in palavra:
        if letra in "aãâáàeêiíoóôõuú":
            letra_p ='p'+ letra
            palavra[indice] = letra +'p'+ letra
    	indice += 1
    palavra = "".join(palavra)
    return palavra
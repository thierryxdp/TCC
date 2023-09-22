def lingua_p(palavra: str) -> str:
    """comentário"""
    palavra = palavra.lower()
    for i in palavra:
        if i in "aãâáàeêiíoóôõuú":
            palavra = list(palavra)
            indice = palavra.index(i)+1 
            letra_p ='p'+ i
            palavra.insert(indice, letra_p)
    palavra = "".join(palavra)
    return palavra
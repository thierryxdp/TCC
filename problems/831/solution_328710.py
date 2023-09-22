def lingua_p(palavra: str) -> str:
    """comentário"""
    indice = 0
    palavra = list(palavra.lower())
    for i in palavra:
        if i in "aãâáàeêiíoóôõuú":
            letra_p ='p'+ i
            
    
    palavra = "".join(palavra)
    indice += 1
    return palavra
def lingua_p(palavra: str) -> str:
    """comentário"""
    
    palavra = list(palavra.lower())
    for i in palavra:
        if i in "aãâáàeêiíoóôõuú":
            
            letra_p ='p'+ i
            palavra.insert(indice, letra_p)
    
    palavra = "".join(palavra)
    return palavra
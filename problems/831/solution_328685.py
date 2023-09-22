def lingua_p(palavra: str) -> str:
    """comentário"""
    
    for i in palavra:
        if i in "aAÃãáÁàÀeéÉEiíÍIoõÕóÓOúÚuU":
            palavra = list(palavra)
            indice = palavra.index(i)+1 
            letra_p ='p'+ i
            palavra.insert(indice, letra_p)
            palavra = "".join(palavra)
    return palavra
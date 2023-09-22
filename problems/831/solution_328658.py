def lingua_p(palavra: str) -> str:
    """comentário"""
    
    for i in palavra:
        if i in "aAÃãáÁàÀeéÉEiíÍIoõÕóÓOúÚuU":
            palavra = list(palavra)
            indice = palavra.index(i) 
            palavra[indice] = 'p'+ i
            palavra = "".join(palavra)
    return palavra
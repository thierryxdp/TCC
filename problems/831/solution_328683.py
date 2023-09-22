def lingua_p(palavra: str) -> str:
    """comentário"""
    
    for i in palavra:
        if i in "aAÃãáÁàÀeéÉEiíÍIoõÕóÓOúÚuU":
            palavra = list(palavra)
            indice = palavra.index(i) 
            letra_p'p'+ i
            palavra.insert(palavra.index(x, i)+1, letra_p)
            palavra = "".join(palavra)
    return palavra
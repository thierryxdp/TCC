def lingua_p(palavra):
    """Funçao que recebe um palavra de entrada str e retorna essa mesma palavra acresentado p antes de todas as vogais e dpois a vogal novamente
    str -> str"""
    p=""
    for i in range(len(palavra)):
        if palavra[i] in "aeiouáéíóúAEIOUÁÉÍÓÚ":
            p = p + palavra[i] + "p" + palavra[i]
        else:
            p = p + palavra[i]
            
    return p.lower()
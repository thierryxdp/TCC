def uppCons(frase:str) -> str:
    """Dada uma frase, a função retorna a mesma frase
    com as consoantes maiúsculas."""
    i = 0
    frase_final = ""
    
    while i < len(frase):
        if str.lower(frase[i]) not in "aãâáàeéiíoóõúu":
            frase_final += str.upper(frase[i])
        else:
            frase_final += frase[i]
        i += 1
    
    return frase_final
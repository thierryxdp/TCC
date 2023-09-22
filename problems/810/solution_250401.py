def inverte(frase):
    """Recebe uma frase e retorna a mesma invertida
    e sem pontuação.
    str -> str"""
    
    if ":" in frase:
        frase = frase.replace(":", "")
    if ";" in frase:
        frase = frase.replace(";", "")
    if "." in frase:
        frase = frase.replace(".", "")
    if "!" in frase:
        frase = frase.replace("!", "")
    if "-" in frase:
        frase = frase.replace("-", "")
    if "," in frase:
        frase = frase.replace(",", "")
    if "?" in frase:
        frase = frase.replace("?", "")
    
    fraselist = frase.split(" ")
    range_list = len(fraselist) + 1
    fat_inv = fraselist[-1:-(range_list):-1]
    inverso = str.join(" ", fat_inv)
    
    return str.lower(inverso)
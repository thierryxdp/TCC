def conta_frases(texto):
    """Função que conta o número de frases em um texto;
    str -> int"""
    if "!"+"?":
        return len(str.split(texto,"!"))+len(str.split(texto,"?"))
    if "!"+"?"+"...":
        return len(str.split(texto,"!"))+len(str.split(texto,"?"))+len(str.split(texto,"..."))
    if "!"+"?"+"..."+".":
        return len(str.split(texto,"!"))+len(str.split(texto,"?"))+len(str.split(texto,"..."))+len(str.split(texto,"."))
    else:
        if".":
            return len(str.split(texto,"."))
        else "...":
            return len(str.split(texto,"..."))
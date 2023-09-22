def conta_frases(texto):
    """Função que conta o número de frases em um texto;
    str -> int"""
    if ".":
        return len(str.partition(texto,"."))
    if "!"+"?":
        return len(str.partition(texto,"!"))+len(str.partition(texto,"?"))
    if "!"+"?"+"...":
        return len(str.partition(texto,"!"))+len(str.partition(texto,"?"))+len(str.partition(texto,"..."))
    if "!"+"?"+"..."+".":
        return len(str.partition(texto,"!"))+len(str.partition(texto,"?"))+len(str.partition(texto,"..."))+len(str.partition(texto,"."))
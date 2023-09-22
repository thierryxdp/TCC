def conta_frases(texto):
    """Funçao que conta o numero de frases que aparecem no texto"""
    lista=[str.replace(texto,"!",".")]
    lista=[str.replace(lista,"?",".")]
    lista=[str.replace(lista,"...",".")]
    lista=[str.split(lista,".")]
    return len(lista)
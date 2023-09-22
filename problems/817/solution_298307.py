def acima_da_media(conjunto):
    """recebe conjunto listado com n e retorna novo conjunto em ordem crescente
    entrada: list, int
    saida: list"""
    list.append(conjunto,5)
    list.sort(conjunto)
    objeto=list.index(conjunto,5)
    conjunto=conjunto[objeto+1:]
    return conjunto
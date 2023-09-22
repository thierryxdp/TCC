def acima_da_media(conjunto):
    """recebe conjunto listado com n e retorna novo conjunto em ordem crescente
    entrada: list, int
    saida: list"""
    list.append(conjunto)
    list.sort(conjunto)
    objeto=list.index(conjunto)
    conjunto=conjunto[objeto+1:]
    return conjunto
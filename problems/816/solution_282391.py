def maiores(conjunto,n):
    """recebe conjunto listado com n e retorna novo conjunto em ordem crescente
    entrada: list, int
    saida: list"""
    list.append(conjunto,n)
    list.sort(conjunto)
    objeto=list.index(conjunto,n)
    conjunto=conjunto[objeto+1:]
    return conjunto
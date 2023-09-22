def faltante(lista):
    """Função que, dada uma lista com a numeração de peças, retorna qual peça está faltando. list -> int"""
    faltando = []
    for p in range(1,len(lista)+2):
        if p not in lista:
            faltando.append(p)
    return faltando[0]
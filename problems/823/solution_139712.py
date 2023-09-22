def faltante(lista):
    """Essa funcao recebe uma lista com a numeração de peças e retorna qual peça esta faltando
    list -> int"""
    faltando = []
    for x in range(1,len(lista)+2):
        if x not in lista:
            faltando.append(x)
    return faltando[0]
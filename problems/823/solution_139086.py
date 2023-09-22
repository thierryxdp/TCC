def faltante(lista):
    """Essa funcao recebe uma lista com a numeração de peças e retorna qual peça esta faltando
    list -> int"""
    faltando = []
    for i in range(1,len(lista)+1):
        if i not in lista:
            faltando.append(i)
    return faltando[0]
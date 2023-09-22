def faltante(lista):
    """Essa funcao recebe uma lista com o numero de peças e retorna qual a peça esta faltando
    list -> int"""
    faltando = []
    for i in range(1,len(lista)+2):
        if i not in lista:
            faltando.append(i)
    return faltando[0]
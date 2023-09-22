def conta_numero(numero,matriz):
    """Funcao que retorna quantas vezes um numero aparece em uma matriz
    int, list --> int"""
    checklist = []
    for i in range(len(matriz)):
        i = -1
        x = list.pop(matriz, i)
        checklist = checklist + x
    return list.count(checklist, numero)
def media_matriz(matriz):
    """Funcao que retorna a media de dos inteiros expressos em
    uma matriz nao vazia
    list --> float"""
    checklist = []
    for i in range(len(matriz)):
        i = -1
        x = list.pop(matriz, i)
        checklist = checklist + x
    total = 0
    n = len(checklist)
    for i in range(len(checklist)):
        y = list.pop(checklist,-1)
        total = total + y
    return round(total/n,2)
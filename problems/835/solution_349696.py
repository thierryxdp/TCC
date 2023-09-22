def melhor_volta(resultados):
    """retorna quemfez a melhor volta, o tempo e volta
    list->tupla"""
    melhorV = []
    for corredor in resultados:
        list.append(melhorV,min(corredor))
    b = min(melhorV)
    a = list.index(melhorV, b)
    c = list.index(resultados[a],b)
    return (a+1,b,c+1)
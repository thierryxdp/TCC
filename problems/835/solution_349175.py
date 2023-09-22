def melhor_volta (resultados):
    """Função que retorna a melhor volta de uma prova e indica a volta e o seu tempo
    list -> tuple"""
    melhor = []
    for i in resultados:
        list.append(melhor, min(i))
    b = min(melhor)
    a = list.index(melhor, b)
    c = list.index(resultados[a], b)
    return (a+1, b, c+1)
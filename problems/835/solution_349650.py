def melhor_volta(Matriz):
    lista = []
    menor = []
    minimo = 0
    ContadorLinhas = 0
    ContadorColunas = 0
    for menor in Matriz:
        lista += [min(menor)]
    minimo = min(lista)
    for linhas in Matriz:
        ContadorLinhas += 1
        if minimo in linhas:
            for colunas in linhas:
                ContadorColunas += 1
                if colunas == minimo:
                    break
            return (CotadorLinhas, minimo, ContadorColunas)
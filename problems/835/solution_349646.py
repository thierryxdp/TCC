def melhor_volta(Matriz):
    lista = []
    menor = []
    minimo = 0
    ContadorLinhas = 0
    ContadorColunas
    for menor in Matriz:
        lista += min(menor)
    minimo = min(lista)
    for linhas in Matriz:
        ContadorLinhas += 1
        if minimo in linhas:
            for colunas in linhas:
                ContaodrColunas += 1
                if colunas == minimo:
                    return (CotadorLinhas, minimo, ContadorColunas)
def melhor_volta(resultados):
    "retorna uma tupla com  os dados referentes a melhor volta da prova, o tempo e qual volta foi a partir da matriz de enrada com os dados dos competidores"
    melhorV = []
    for corredor in resultados:
        list.append(melhorV,min(corredor))
    b = min(melhorV)
    a = list.index(melhorV, b)
    c = list.index(resultados[a],b)
    return (a+1,b,c+1)
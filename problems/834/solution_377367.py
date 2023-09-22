def media(matriz):
    "retorna a media de todos os numeros da matriz da entrada"
    med = 0
    for linha in matriz:
        for elemento in linha:
            med = med + elemento
        conta = med/(len(matriz)*len(matriz[0]))
    return round(conta,2)
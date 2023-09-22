def media_matriz(matriz):
    assert (len(matriz)>0) and (len(matriz[0])>0)
    soma =0
    qt =0
    for linha in matriz:
        for elemento in linha:
            soma= soma+ elemento
            qt = qt + 1
    return soma/qt
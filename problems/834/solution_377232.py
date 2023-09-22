def media_matriz(matriz):
    
    soma=0
    qnt_numeros=0
    for linha in matriz:
        for numero in linha:
            qnt_numeros+=1
            soma+=numero
    media=soma/qnt_numeros
    return media
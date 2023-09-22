#Entrada: Uma matriz
#1)Precisamos contar o número de elementos da matriz
#2)Precisamos também somar todos os elementos
#3)Ao final, dividiremos a soma pela quantidade de elementos
#4)Fazendo isso, obteremos a média
#5)Com isso, é só arredondar e retornar
def media_matriz(matriz:list)->float:
    """Recebe uma matriz e diz a média entre os elementos"""
    soma=0
    contador=0
    for linha in matriz:
        for elemento in linha:
            soma+=elemento
            contador+=1
    return round(soma/contador,2)
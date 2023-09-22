'''Ao receber um número inteiro e uma matriz, o programa procura
pelo número na matriz, e retorna a quantidade de vezes
 que ele aparece '''

def conta_numero(numero, matriz):
    for elemento in matriz:
        if len(matriz) > 1:
            for subelemento in elemento:
                return list.count(subelemento, numero)
        else:
            return list.count(elemento, numero)
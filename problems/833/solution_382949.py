'''Ao receber um número inteiro e uma matriz, o programa procura
pelo número na matriz, e retorna a quantidade de vezes
 que ele aparece '''

def conta_numero(numero, matriz):
    acumulador = ()
    for elemento in matriz:
        acumulador = acumulador + (list.count(elemento, numero),)
	return sum(acumulador)
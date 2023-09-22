def qtd_divisores(numero):
	'''Função que dado um número, contabiliza quantos divisores ele possui.
	Entrada: int
	Saída int'''
	divisores=0

    for analisado in range(numero):
        if numero%(analisado+1)==0:
            divisores+=1
            analisado+=1

    return divisores
#Soma H
def soma_h(n):
	#Faça uma função chamada **soma_h** para calcular e retornar o valor H com N termos onde N é inteiro e dado com entrada.
    soma = 0
    for i in range(1,n+1):
        soma += 1/i
    soma = round(soma, 2)

    return soma
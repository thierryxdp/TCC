#Números primos
def primo(num):
	#Função que dado um número inteiro positivo, verifique se este número é primo ou não. 
    p = True
    for i in range(1, num//2):
        if (num % i == 0):
            p = False
            break

    return p
#Divisores
def divisores(n):
	#Função que conte quantos divisores um número tem. Este número será passado como entrada.
    cont_div = 0
    for i in range(1, n+1):
        if(n % i == 0):
          cont_div += 1
    
    return cont_div
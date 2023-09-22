#Função que retorna a quantidade de divisores, dado um número n.
def qtd_divisores(n):
    divisores = 0
    #loop para percorrer todos os números de 1 até n.
    for i in range(1, n+1):
        #Caso o resto da divisão de n por i seja igual a zero, significa que i é um divisor de n, logo, o número de divisores recebe um incremento
        if n%i == 0:
            divisores+=1
    #retorna o número de divisores
    return divisores
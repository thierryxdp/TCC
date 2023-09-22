def soma_h(N):
    """função que calcula o valor de H com N termos onde o N é um número inteiro e retorna o resultado com duas casas decimais
	int -> float"""
    
    soma = 0 
    
    for i in range(1,N+1):
        soma = soma + 1/i
       
    return round(soma,2)
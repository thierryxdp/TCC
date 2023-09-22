def divisao(n):
    
    return 1/n

def soma_h(n: int) -> float:
    """Função que, dada a entrada como sendo um número inteiro, retorna o somatório de 
    1 + 1/2 + ... + 1/n"""
    
	numero = list(map(divisao, n))
    str_somatorio = str(somatorio)
	str_final = str(str_somatorio)[1:-1]
    usar = float(str_final)
    
    soma = 0

    for i in range(1, n):
        soma = soma + (1 / i)

    somatorio_final = soma + usar
    
    return round(somatorio_final, 2)
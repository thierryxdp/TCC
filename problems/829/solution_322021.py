def soma_h(N):		
    """Função que calcula e retorna o valor de H com N termos"""
    
    soma=0
    for s in range(1, N+1):
        soma = soma+1/s
    return round(soma,2)
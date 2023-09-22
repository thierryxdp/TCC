def divisao(n):
    
    return 1/n

def soma_h(n: int) -> float:
    """Função que, dada a entrada como sendo um número inteiro, retorna o somatório de 
    1 + 1/2 + ... + 1/n"""
    
    numero = [n]
    somatorio = list(map(divisao, numero))  
    str_somatorio = str(somatorio)
    str_final = str(str_somatorio)[1:-1]
    
    return float(str_final)
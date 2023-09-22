# Dado um número inteiro N, esta função calcula o valor de H, como 
# H = 1 + 1/2 + 1/3 + ... + 1/N, retornando o resultado com 2 casas decimais
# int -> float

def soma_h(N):
    H = 0
    
    for i in range(1,N+1):
        H += 1/i
        
    return round(H,2)
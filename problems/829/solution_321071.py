# Dado um número inteiro N, esta função calcula o valor de H, como 
# H = 1 + 1/2 + 1/3 + ... + 1/N, retornando o resultado com 2 casas decimais
# int -> float

def inverso(n):
    return 1/n

def soma_h(N):
    H = sum(list(map(inverso,list(range(1,N+1)))))  
    return round(H,2)
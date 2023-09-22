qtd_divisores(n)
divisores=0
while i < n//2:
    if n%i == 0:
        divisores = divisores + 1
    return divisores
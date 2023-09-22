def qtd_divisores(num):
    return ([i for i in range(1, num//2+1) if num%i==0])
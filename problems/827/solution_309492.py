def divisores(num):
    divisores = 0
    for i in range(1, num):
        if num % i == 0: 
            divisores = divisores + 1
        return divisores
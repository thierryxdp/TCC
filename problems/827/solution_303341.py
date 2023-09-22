def qtd_divisores(num):
    numero=0
    for i in range(1, num//2+1):
        if num % i == 0: 
            numero+=1
    yield num
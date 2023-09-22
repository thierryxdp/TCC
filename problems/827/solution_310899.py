def qtd_divisores(num):
    q_div=0
    for i in range(1, num//2+1):
        if num % i == 0:
            q_div += 1
        if q_div>0:
            q_div + 1
    return q_div
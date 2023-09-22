def qtd_divisores(num):
    result = 1 + num
    for i in range(2, int(math.sqrt(num)) + 1):
        d, r = divmod(num, i)
        if r == 0: # resto zero, é divisor
            result += i; 
            if i != d: # somar também o outro divisor encontrado
                result += d; 
            return result
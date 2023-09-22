def qtd_divisores(n):
    num_div = 0 # estou contando o 1 e o n como divisores de n
    
    for i in range(1, n + 1):
        if (n == 0):
            return 0
        
        elif (n % i == 0):
            num_div += 1
    
    return num_div
def qtd_divisores(n):
    num_div = 2 # estou contando o 1 e o n como divisores de n
    
    for i in range(2,n):
        if (n % i == 0):
            num_div += 1
    
    return num_div
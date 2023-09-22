def qtd_divisores(num):
    """Função que calcula a quantidade de divisores que um numero tem,int-->int"""
     for i in range(int(num/2+1)):
        if num % i == 0: 
            i = i +1
    return num
def qtd_divisores(n):
    '''
    Programa que lê um inteiro positivos n 
    e verifica e imprime seus divisores int--> int.
    '''
    for i in range(1, int(n/2+1)):
        if n % i == 0: 
        i+=i
    return n
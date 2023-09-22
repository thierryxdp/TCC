def qtd_divisores(num):
    """Recebe um numero e retorna a quantidade de divisores que tem;
    float --> int"""

    cont = 0
    
    for iii in range(1,num + 1):
        if (num % iii == 0):
            cont += 1
            
    return cont
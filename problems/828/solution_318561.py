def primo(num):
    """ Dado um numero verifica se o número é primo..
    entrada intero -> booleando"""
    
    d = list(range(3,num,2))
    qtd_divisores = 0
    
    if num == 2:
        qtd_divisores == 0
    
    for proximo in d:
        if num%proximo == 0:
            qtd_divisores = qtd_divisores + 1 
    return qtd_divisores == 0
def fatorial(num):
    """retorna o fatorial de um numero""" 
    if num < 0: 
        return "o fatorial nao existe"

    elif num == 0: 
        return 1
        
    else: 
        fatorial = 1
        while(num > 1): 
            fatorial *= num 
            num -= 1
        return fatorial
def fatorial(numero:int) -> int:
    """Função calcula o fatorial do número
    
       Parameters:
       numero: número inteiro qualquer
       
       Returns:
       valor do fatorial do número inserido
    """
    i = 1
    mult = 1

    while i <= numero:
        mult = mult * i
        i = i + 1
    return mult
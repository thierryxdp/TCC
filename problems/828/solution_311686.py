def primo(numero:int) -> bool:
    """Função indica se o valor inserido é primo ou não

       Parameters:
       numero: número inteiro qualquer
       
       Returns:
       True para numero é primo e False para numero não é primo
    """
    qtd_divisores = 0
    
    for n in range(1,numero + 1):
        if numero%n == 0:
            qtd_divisores += 1
            
    if qtd_divisores == 2:
        return True
    else:
        return False
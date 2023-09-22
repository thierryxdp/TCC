def qtd_divisores(numero:int) -> int:
    """Função conta quantos divisores o número inserido tem
    
       Parameters:
       numero: número inteiro qualquer
       
       Returns:
       quantidade de divisores do número inserido
    """
    qtd = 0
    for n in range(1,numero + 1):
        if numero%n == 0:
            qtd += 1
    return qtd
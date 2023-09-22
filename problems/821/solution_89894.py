def fatorial(n):
    
    """Função que calcula o fatorial de um número
    inteiro qualquer. int -> int """
    
    cont = n
    fat = 1
    
    while cont > 0:
        fat = fat * cont
        cont = cont - 1
    return fat
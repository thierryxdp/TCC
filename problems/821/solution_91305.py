def fatorial(num):
    """ Função que recebe um numero e retorna o fatorial
    dele.
    Entrada: int
    Saída: int"""    
    while num > 0:
        fat = 1
        while num > 1:
            fat = fat  * num
            num = num - 1
        return fat
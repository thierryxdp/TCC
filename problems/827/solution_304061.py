def qtd_divisores(numero):
    '''Retorna quantos divisores um numero tem;
       Entrada: int;
       Saida: int;
    '''
    divisor = 1
    if divisor <= numero:
        x = numero%divisor == 0
        lista = [x]
    return len(lista)
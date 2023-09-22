def primo(n):
    """Dado n, sendo n inteiro e positivo, retorna dizendo se n é primo
    ou não através de um número booleano.
    assinatura: int --> int
    testes:
    """
    return qtd_divisores(num) == 2
    
def qtd_divisores(num):
    contador = 0
    if num > 0:
        for i in range(1, 10000):
            if num%i == 0:
                contador = contador + 1
        return contador  
    if num <= 0:
        return 0
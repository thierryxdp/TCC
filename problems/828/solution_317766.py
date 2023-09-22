def qtd_divisores(num):
    contador = 0
    if num > 0:
        for i in range(1, 10000):
            if num%i == 0:
                contador = contador + 1
        return contador  
    if num <= 0:
        return 0
    
def primo(num):
    """Dado n, sendo n inteiro e positivo, retorna dizendo se n é primo
    ou não através de um número booleano.
    assinatura: int --> bool
    testes:
    primo(3) == True
	primo(8) == False
	primo(7) == True
    """
    return qtd_divisores(num) == 2
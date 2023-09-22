def primo(numero):
    """ Função que dado um número inteiro positivo, verifca
        se este número é primo ou não. Retorna um valor
        booleano;
        int -> bool"""
    for i in range(2,numero):
        if numero%i == 0:
            return False
    return True
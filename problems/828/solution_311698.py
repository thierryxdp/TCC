def primo(numero):
    """Função que dado um número inteiro positivo, verifica se este número é primo ou não
       float -> bool"""
    multiplo = 0
    for contador in range(2,numero):
        if (numero%contador == 0):
            return "False"
        multiplo += 1
    if multiplo == 0:
        return "True"
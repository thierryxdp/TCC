def primo(num):
    """
    Função que recebe um número inteiro positivo e verifica se ele é primo ou não.
    int -> bool
    """
    
    qnt_divisores = 0
    numeros = list(range(1,num+1))
    
    for elemento in numeros:
        if (num%elemento == 0):
            qnt_divisores = qnt_divisores + 1
        elif (qnt_divisores <= 2):
            return True
        else:
            return False
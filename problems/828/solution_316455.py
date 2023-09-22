def primo(n):
    """ Função que recebe um númeiro inteiro positivo e veri-
    fica se ele é primo ou não. Se o número em questão for pri-
    mo a função retornará True, caso contrário ela retornará 
    False.
    
    int - bool
    """
    
    qtd_divisores = 0
    for i in range(2,n):
        if n%i == 0:
            qtd_divisores =  qtd_divisores + 1
    return qtd_divisores==2
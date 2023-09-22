def primo(n):
    """ Função que recebe um númeiro inteiro positivo e veri-
    fica se ele é primo ou não. Se o número em questão for pri-
    mo a função retornará True, caso contrário ela retornará 
    False.
    
    int - bool
    """
    
    i = 0
    while i < len(range(2,n)):
        m = n%i == 0
        i = i+1
    return m
def primo(num):
    """ Dado um número qualquer retorna se determinado número é primo ou não;
    int-> bool """
    for i in list(range(2,num)):
        if num%i==0 and i!=num:
            return False
    return True
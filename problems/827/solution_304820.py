def qtd_divisores(numero_inteiro):

    """ Função que indica quantos divisores um dado número inteiro possui.
        int -> int
    """

    qtd_divisores = 0

    for n in range(1,numero_inteiro+1):
        
        if numero_inteiro%n == 0:
            
            qtd_divisores = qtd_divisores + 1
            
    return qtd_divisores
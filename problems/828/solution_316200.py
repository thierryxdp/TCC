def primo(numerointeiro):
    """A entrada, que está no parâmetro, é um número postivo
    inteiro e o retorno será dizer se este número é primo ou
    não, usando um valor booleano para isso."""
    #int -> bool
    numerofinal = numerointeiro >= 2
   
    for i in range(1, numerofinal -1):
             if numerofinal % i == 0:
                return True
             else:
                return False
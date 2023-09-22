def primo(numerointeiro):
    """A entrada, que está no parâmetro, é um número postivo
    inteiro e o retorno será dizer se este número é primo ou
    não, usando um valor booleano para isso."""
    #int -> bool
   
    
    for i in range(2, numerointeiro):
             if numerointeiro % i == 0 and i:
                return False
    else:
                return True
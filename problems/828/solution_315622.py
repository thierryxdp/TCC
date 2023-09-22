def primo(numero):
    """
    	Função que retorna se o número positivo dado é primo
        ou não.
    	int -> booleano
    """
    multiplos = 0
    for x in range(2,numero):
        if numeros%x == 0:
            multiplos += 1    
    if multiplos==0:
        return True
    else:
        return False
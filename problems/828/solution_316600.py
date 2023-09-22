def primo(numero):
    """Recebe um número e diz se ele é primo ou não;
    	int -> bool"""
    qtd=0
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            qtd=qtd+1
    if qtd>2:
        return False
    else:
        return True
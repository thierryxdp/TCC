def primo(numero):
    """ função que recebe um número inteiro e positivo, verifica se este número é prmimo ou nao.
    	retorna um valor booleano. int --> boolean """
    
    divisor = 2
    while divisor < numero:
        if numero%divisor == 0:
            return False
        divisor += 1
        
    return True
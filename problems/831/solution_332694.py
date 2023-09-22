def lingua_p(palavra):
    """ Recebe uma palavra em português e traduz
    para a língua do P.
    Assintatura: str--> str 
    Testes:
    """
    
    palavra_p =''
    for letra in palavra:
        if letra in 'AEIOUaeiouáéíóú':
        	 palavra_p+=letra+'p'+letra
        else:
             palavra_p+=letra
    return  palavra_p
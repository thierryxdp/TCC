def fatorial(numero):
    """Calcula o fatorial deste número.
       int -> int"""
    
    fat = 1
    i = 0
    
    while i <= numero:
        fat = fat*i
        i = i + 1
        
        return fat
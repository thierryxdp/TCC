def primo (n):
    """Função que retorna se um número dado é primo ou não"""
    """int -> bool"""
    multiplos = 0
    
    for count in range(2,n):
        if (n % count == 0):
            multiplos += 1
        
    if (multiplos == 0):
            return True
    else:
            return False
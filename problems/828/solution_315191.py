def primo (n):
    """ """
    """ """
    multiplos = 0
    
    for count in range(1,n+1):
        if (n % count == 0):
            multiplos += 1
        
    if (multiplos == 0):
            return True
    else:
            return False
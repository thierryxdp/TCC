def primo(num):
    """Função que determina se um número é primo ou não.
signature: integer --> bool
"""
    for x in range (2, num, 1):
        if num % x == 0:
       		return False
    	#if num % x != 0:
        #    return True
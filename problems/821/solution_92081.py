def fatorial(n):
    """Recebe um valor inteiro n e calcula  n!
    assinatura: int --> int
    """
    
    for i in list(range(1, n)):
    	res=0
        res+=n*i
        
    return res
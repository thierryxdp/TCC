def fatorial(n):
    """Recebe um valor inteiro n e calcula  n!
    assinatura: int --> int
    """
    res=0
    for i in list(range(1, n)):
    	res+=n*i
        
    return res
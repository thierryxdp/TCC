def fatorial(n):
    """Recebe um valor inteiro n e calcula  n!
    assinatura: int --> int
    """
    res=n
    for i in list(range(1, n)):
    	if i <=n:
            res=n*i
        
    return res
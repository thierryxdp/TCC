def soma_h(n):
    """Função que calcula  a soma  como un inteuro como base
    int -> int"""
     h = 0
        for i in range(1 ,n+1):
            h = h +float(1//n)
        return round (h, 2)
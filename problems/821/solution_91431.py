def fatorial(n):
   '''Calcula o fatorial de um número n.
   Assinatura: int->int'''
    res=1
    for x in range(n):
        res = res*(x+1)
    return res
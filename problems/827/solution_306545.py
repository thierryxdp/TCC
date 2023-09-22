def filtro(n):
    'Verifica se num é divisivel por n'
    global n
    return n%x == 0

def qtd_divisores(n):
   
    
    quantidade = filter(lambda x: n%x == 0,range(1,n+1))
    return len(quantidade)
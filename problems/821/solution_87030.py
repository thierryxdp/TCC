def fatorial(num):
    """Dado um numero, retorna o fatorial desse numero"""
    """entrada: int
    saida: int"""
    
    pos=0
    num_fatorial=1
    lista=  list(range(num,0,-1))
    
    while pos < len(lista):
    	num_fatorial = num_fatorial*lista[pos]
        pos = pos+1
    return num_fatorial
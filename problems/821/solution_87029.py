def fatorial(num):
    """Dado um numero, retorna o fatorial desse numero"""
    """entrada: int
    saida: int"""
    
    pos=0
    resultado=1
    lista=  list(range(num,0,-1))
    
    while pos < len(lista):
    	resultado = resultado*lista[pos]
        pos = pos+1
    return resultado
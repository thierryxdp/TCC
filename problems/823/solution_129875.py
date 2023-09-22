def faltante(lista):
    """Funçao que dado uma lista faltando um numero reconstroi a lista completa e retorna o numero que falta na lista
    list -> int"""
    
    quantidade = len(lista)
    lista_completa = list(range(0,quantidade+2))
    numero_faltante = sum(lista_completa)- sum(lista)
    
   
    
    return  numero_faltante
def faltante(lista):
    quantidade = len(lista)
    lista_completa = list(range(0,quantidade+2))
    a=sum(lista_completa)
    b=sum(quantidade)
    
    return a - b
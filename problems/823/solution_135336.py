def faltante(n): 
    '''funçao que identifica qual peça do quebra cabeça falta com base na lista de entrada''' 
    '''list->int'''
    i=0
    resultado=()
    while i < len(n):
        if n[i]==i+1:
            resultado=n[i]+1
        i=i+1 
    return resultado
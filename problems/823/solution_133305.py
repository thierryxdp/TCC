def faltante(n: list) -> int:
    
    lista_completa = [*range(1, n[-1]+1)]
    
    i = 0
    
    while i < len(lista_completa):
        
        if not i[lista_completa] == i[n]:
            return i[lista_completa]
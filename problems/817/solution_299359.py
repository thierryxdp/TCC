def maiores(lista_numero,n):
    
    if n not in lista_numero:
        lista_numero = lista_numero + [n]
        
        lista_numero = sorted(lista_numero)
        
        x = list.index(lista_numero,n)
        
        return lista_numero[(x+1):len(lista_numero)]
    
    else:
        lista_numero = sorted(lista_numero)
        
        x = list.index(lista_numero,n)
        
        return lista_numero[(x+1):len(lista_numero)]

def acima_da_media(notas):
    
    media = sum(notas) / len(notas)
    return maiores(nota,media)
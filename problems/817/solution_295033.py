def acima_da_media(notas:list) -> list:
    """comentário"""
    media = sum(notas)/len(notas)
    return maiores(notas, media)

def maiores(lista: list, n:int) -> list:
    """Essa função, dada uma lista de números e um número inteiro n, 
    retorna outra lista contendo todos os números da lista original
    maiores que n"""
    lista2 = lista.copy()
    lista2.append(n)
    lista2 = sorted(lista)
    i = lista2.index(n)
    
    if max(lista) == n:
        return []
    
    elif min(lista) == n:
        lista.remove(n)
        return (lista)
    
    else:
        lista.remove(lista2[i])
        maiores = lista2[i:]
        return (maiores)
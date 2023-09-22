def maiores (lista_numero, n):
    """recebe uma lista de numeros inteiros e um outro inteiro n, e retorna
    uma lista contendo todos os elementos da lista origial maiores do que n
    list, int -> list"""
    
    if n not in lista_numero:
        lista_numero = lista_numero + [n]
        
        lista_numero = sorted(lista_numero)
        
        x = list.index(lista_numero, n)
        
        return lista_numero[(x+1):len(lista_numero)]
    
    else:
        x = list.index(lista_numero, n)
        
        return lista_numero[(x+1):len(lista_numero)]


def acima_da_media (notas):
    """recebe uma lista contendo as notas dos alunos de uma sala, calcula a 
    media entre elas e retorna umas lista ordenada contendo aquelas que ficaram
    acima da media
    list -> list"""
    
    media = sum(notas) / len(notas)
    
    return maiores(notas, media)
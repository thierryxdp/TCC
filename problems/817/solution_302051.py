def maiores(lista,n):
    """..."""
    listafinal=[]
    list.append(lista,n)
    for x in range(len(lista)):
        if lista[x] > n:
            listafinal.append(lista[x])  
    return sorted(listafinal)
    
    
    
def acima_da_media(notas):
    """Recebe uma lista com as notas dos alunos e retorna
    uma nova lista ordenada com as notas acima da média.
    Assinatura: list -> list"""
    media=sum(notas)/(len(notas))
    return maiores(notas,media)
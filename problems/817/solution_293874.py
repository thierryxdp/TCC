def maiores(lista,n):
    if n not in lista:
        list.append(lista,n)
        list.sort(lista)
        ind = list.index(lista,n)
        listaf=lista[ind+1:]
        
        return lista f
    
def acima_da_media(lista):
    """Função que avalia as notas dos alunos e retorna os alunos com nota acima da media
    list -> list"""
    
    media = sum(lista)/len(lista)
    
    return maiores(lista,media)
def acima_da_media(lista,n):
    
    if n not in lista:
        lista.append(n)
    lista.sort()
    i = lista.index(n)
    return lista[i+1:]    

def acimaDaMedia2(notas):
    """função que recebe uma lista com as notas dos alunos de uma turma e retorna
    uma lista ordenada com as notas que ficaram acima da média.
    list -> list"""
    media = sum(notas)/len(notas)
    return acima_da_media(notas, media)
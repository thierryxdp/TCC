def maiores(lista,n):
    lista.append(n+1)
    lista.sort()
    i = lista.index(n+1)
    return lista[i+1:]
def acima_da_media(lista):
    """
    Função que recebe uma lista de notas de uma turma e retorna 
    uma lista das notas que ficaram acima da média
    
    list ---> list
    """
    media = sum(lista)/len(lista)
    return maiores(lista,media)